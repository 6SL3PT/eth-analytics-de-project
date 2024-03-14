INSERT INTO 
    block_price
SELECT
    number AS block,
    size,
    gas_limit_wei,
    gas_used_wei,
    transaction_count,
    base_fee_per_gas_gwei,
    base_fee_per_gas_gwei * (gas_used_wei / POWER(10,9)) AS burned_eth,
    block_timestamp,
    CAST(static_rewards_eth AS SMALLINT) AS static_rewards_eth,
    validator_withdrawals_eth,
    price
FROM 
    (
        SELECT 
            b.number,
            b.size,
            b.gas_limit AS gas_limit_wei,
            b.gas_used AS gas_used_wei,
            b.transaction_count,
            IFNULL(b.base_fee_per_gas, 0) / POWER(10,9) AS base_fee_per_gas_gwei,
            TO_TIMESTAMP(
                REPLACE(REPLACE(b.item_timestamp, 'T', ' '), 'Z', ''), 
                'yyyy-MM-dd HH:mm:ss') AS block_timestamp,
            CASE 
                WHEN b.number < 4370000 THEN 5
                WHEN b.number >= 4370000 AND b.number < 7280000 THEN 3
                WHEN b.number >= 7280000 AND b.number < 15537393 THEN 2
                ELSE 0
            END AS static_rewards_eth,
            IFNULL(b.withdrawals_amount, 0) / POWER(10,9) AS validator_withdrawals_eth,
            CAST(REPLACE(p.price, 'n', '') AS DECIMAL(24, 8)) / POWER(10, 8) AS price
        FROM blocks b, prices p
        WHERE b.number = p.block
    )
