\connect postgres

-- create a ethereum schema
CREATE SCHEMA ethereum;

-- create a table named block_price
CREATE TABLE ethereum.block_price (
    block INT PRIMARY KEY,
    size INT,
    gas_limit_wei INT,
    gas_used_wei INT,
    transaction_count INT,
    base_fee_per_gas_gwei DECIMAL(16, 9),
    burned_eth DECIMAL(16, 9),
    block_timestamp TIMESTAMP NOT NULL,
    static_rewards_eth SMALLINT,
    validator_withdrawals_eth DECIMAL (16, 9),
    price DECIMAL(16, 8) NOT NULL
);
CREATE INDEX idx_ethereum_block_price_block ON ethereum.block_price(block);

CREATE TABLE ethereum.transactions (
    minute_group_id VARCHAR(12) PRIMARY KEY,
    block_timestamp TIMESTAMP NOT NULL,
    avg_gas_price_gwei DECIMAL(32, 16),
    tx_fees_eth DECIMAL(32, 16),
    volume_eth DECIMAL(32, 16),
    active_address INT
);
CREATE INDEX idx_ethereum_transaction_minute ON ethereum.transactions(minute_group_id);

-- create grafana user with only reading privileges
CREATE USER grafana_reader WITH PASSWORD 'grafana';
GRANT CONNECT ON DATABASE postgres TO grafana_reader;

GRANT SELECT ON ALL TABLES IN SCHEMA ethereum TO grafana_reader;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA ethereum TO grafana_reader;
GRANT USAGE ON SCHEMA ethereum TO grafana_reader;
ALTER DEFAULT PRIVILEGES IN SCHEMA ethereum GRANT SELECT ON TABLES TO grafana_reader;
