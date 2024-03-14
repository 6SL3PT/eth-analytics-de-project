CREATE TABLE blocks (
    number INT NOT NULL,                --18525742
    size INT,                           --107451
    gas_limit INT,
    gas_used INT,                       --12521957
    item_timestamp VARCHAR(32) NOT NULL,
    transaction_count INT,
    base_fee_per_gas BIGINT,
    withdrawals_amount BIGINT
) WITH (
    'connector' = '{{ connector }}',
    'topic' = '{{ topic }}',
    'properties.bootstrap.servers' = '{{ bootstrap_servers }}',
    'properties.group.id' = '{{ consumer_group_id }}',
    'scan.startup.mode' = '{{ scan_stratup_mode }}',
    'format' = '{{ format }}'
);