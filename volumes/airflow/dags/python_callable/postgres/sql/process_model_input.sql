WITH T AS (  
    SELECT block_timestamp::date AS block_timestamp,
        block,
        price
    FROM ethereum.block_price
    WHERE block_timestamp::date <= now()::date - 1
),
OHLC AS (
    SELECT MMV.block_timestamp,
        O.price as open,
        high,
        low,
        C.price as close
    FROM
        (
            SELECT block_timestamp,
                MAX(price) AS high,
                MIN(price) AS low
            FROM T
            GROUP BY block_timestamp
        ) MMV,
        (
            SELECT DISTINCT ON (block_timestamp) block_timestamp, block, price
            FROM T
            ORDER BY block_timestamp, block DESC
        ) C,
        (
            SELECT DISTINCT ON (block_timestamp) block_timestamp, block, price
            FROM T
            ORDER BY block_timestamp, block
        ) O
    WHERE MMV.block_timestamp = C.block_timestamp 
        AND MMV.block_timestamp = O.block_timestamp
    ORDER BY MMV.block_timestamp DESC
    LIMIT 52
),
ICHIMOKU AS (
    SELECT block_timestamp,
        (MAX(close) OVER (ORDER BY block_timestamp ROWS BETWEEN 8 PRECEDING AND CURRENT ROW) + 
            MIN(close) OVER (ORDER BY block_timestamp ROWS BETWEEN 8 PRECEDING AND CURRENT ROW)) / 2 
            AS "Tenkan Sen",
        (MAX(close) OVER (ORDER BY block_timestamp ROWS BETWEEN 25 PRECEDING AND CURRENT ROW) + 
            MIN(close) OVER (ORDER BY block_timestamp ROWS BETWEEN  25 PRECEDING AND CURRENT ROW)) / 2 
            AS "Kijun Sen",
        (MAX(close) OVER (ORDER BY block_timestamp ROWS BETWEEN 51 PRECEDING AND CURRENT ROW) + 
            MIN(close) OVER (ORDER BY block_timestamp ROWS BETWEEN 51 PRECEDING AND CURRENT ROW)) / 2 
            AS "Senkou Span B"
    FROM (SELECT * FROM OHLC ORDER BY block_timestamp)
),
ALLIGATOR AS (
    SELECT block_timestamp,
        AVG(close) OVER (ORDER BY block_timestamp ROWS BETWEEN 21 PRECEDING AND 8 PRECEDING) AS "Jaw",
        AVG(close) OVER (ORDER BY block_timestamp ROWS BETWEEN 8 PRECEDING AND 3 PRECEDING) AS "Lips"
    FROM (SELECT * FROM OHLC ORDER BY block_timestamp)
),
TX AS (
    SELECT TX.block_timestamp::date AS "block_timestamp",
        SUM(tx_count) AS "tx_count",
        CAST(SUM(volume_eth * price) AS DECIMAL(32, 12)) AS "volume_usd"
    FROM ethereum.transactions TX, ethereum.block_price BP
    WHERE date_bin('1 minute', TX.block_timestamp, TIMESTAMP '2001-01-01') = date_bin('1 minute', BP.block_timestamp, TIMESTAMP '2001-01-01')
    GROUP BY TX.block_timestamp::date
)
INSERT INTO ethereum.model_input(
    block_timestamp, volume_usd, tx_count, senkou_span_sub, alligator_sub
) SELECT TX.block_timestamp, 
    "volume_usd",
    "tx_count",
    ("Tenkan Sen" + "Kijun Sen") / 2 - "Senkou Span B" AS "senkou_span_sub",
    "Lips" - "Jaw" AS "alligator_sub"
FROM TX, ICHIMOKU, ALLIGATOR
WHERE TX.block_timestamp::date = now()::date - 1
    AND TX.block_timestamp = ICHIMOKU.block_timestamp
    AND TX.block_timestamp = ALLIGATOR.block_timestamp