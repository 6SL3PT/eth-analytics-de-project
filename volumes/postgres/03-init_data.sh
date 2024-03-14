#!/bin/bash

# Import block_price data
for FILE in $(ls /docker-entrypoint-initdb.d/data/block_price)
do
    COMMAND="\copy ethereum.block_price FROM '/docker-entrypoint-initdb.d/data/block_price/$FILE' WITH (FORMAT CSV)"
    PGPASSWORD=$POSTGRESQL_PASSWORD psql -U $POSTGRESQL_USERNAME -d $POSTGRESQL_DATABASE -c "$COMMAND" &> /dev/null

    echo File: $FILE - import to table 'ethereum.block_price' successfully
done

# Import transactions data
for FILE in $(ls /docker-entrypoint-initdb.d/data/transactions)
do
    COMMAND="\copy ethereum.transactions FROM '/docker-entrypoint-initdb.d/data/transactions/$FILE' WITH (FORMAT CSV)"
    PGPASSWORD=$POSTGRESQL_PASSWORD psql -U $POSTGRESQL_USERNAME -d $POSTGRESQL_DATABASE -c "$COMMAND" &> /dev/null

    echo File: $FILE - import to table 'ethereum.transactions' successfully
done