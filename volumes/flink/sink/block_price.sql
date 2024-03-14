CREATE TABLE block_price (
    block INT NOT NULL,
    size INT,
    gas_limit_wei INT,
    gas_used_wei INT,
    transaction_count INT,
    base_fee_per_gas_gwei DECIMAL (16,9),
    burned_eth DECIMAL (16,9),
    block_timestamp TIMESTAMP NOT NULL,
    static_rewards_eth SMALLINT,
    validator_withdrawals_eth DECIMAL (16,9),
    price DECIMAL(16, 8) NOT NULL,
    PRIMARY KEY (block) NOT ENFORCED
) WITH (
    'connector' = 'jdbc',
    'url' = 'jdbc:postgresql://postgres:5432/postgres',
    'table-name' = 'ethereum.block_price',
    'username' = 'postgres',
    'password' = 'postgres',
    'driver' = 'org.postgresql.Driver'
);