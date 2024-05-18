\connect postgres

-- create a ethereum schema
CREATE SCHEMA ethereum;

-- create a table named block_price (stream)
CREATE TABLE ethereum.block_price (
    block INT PRIMARY KEY,
    size INT,
    gas_limit_wei INT,
    gas_used_wei INT,
    transaction_count INT,
    base_fee_per_gas_gwei DECIMAL(16, 9),
    burned_eth DECIMAL(16, 9),
    block_timestamp TIMESTAMPTZ NOT NULL,
    static_rewards_eth SMALLINT,
    validator_withdrawals_eth DECIMAL (16, 9),
    price DECIMAL(16, 8) NOT NULL
);
CREATE INDEX idx_ethereum_block_price_ts_brin ON ethereum.block_price USING BRIN (block_timestamp);

-- create a table named transactions (batch)
CREATE TABLE ethereum.transactions (
    minute_group_id VARCHAR(12) PRIMARY KEY,
    block_timestamp TIMESTAMPTZ NOT NULL,
    avg_gas_price_gwei DECIMAL(32, 16),
    tx_count INT,
    tx_fees_eth DECIMAL(32, 16),
    volume_eth DECIMAL(32, 16),
    active_address INT
);
CREATE INDEX idx_ethereum_transaction_ts_brin ON ethereum.transactions USING BRIN (block_timestamp);

-- create a table named model_input (batch)
CREATE TABLE ethereum.model_input (
    model_input_id SERIAL PRIMARY KEY,
    block_timestamp TIMESTAMPTZ NOT NULL,
    volume_usd DECIMAL(32, 12),
    tx_count BIGINT,
    senkou_span_sub DECIMAL(32, 16),
    alligator_sub DECIMAL(32, 16)
);
CREATE INDEX idx_ethereum_model_input_ts_brin ON ethereum.model_input USING BRIN (block_timestamp);

-- create table named model_prediction
CREATE TABLE ethereum.model_prediction (
    model_prediction_id SERIAL PRIMARY KEY,
    block_timestamp TIMESTAMPTZ NOT NULL,
    predict_result DECIMAL(16, 8) NOT NULL
);
CREATE INDEX idx_ethereum_model_prediction_ts_brin ON ethereum.model_prediction USING BRIN (block_timestamp);

-- create grafana user with only reading privileges
CREATE USER grafana_reader WITH PASSWORD 'grafana';
GRANT CONNECT ON DATABASE postgres TO grafana_reader;

GRANT SELECT ON ALL TABLES IN SCHEMA ethereum TO grafana_reader;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA ethereum TO grafana_reader;
GRANT USAGE ON SCHEMA ethereum TO grafana_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA ethereum GRANT SELECT ON TABLES TO grafana_reader;
