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

# Import model_input data
for FILE in $(ls /docker-entrypoint-initdb.d/data/model_input)
do
    COMMAND="\copy ethereum.model_input FROM '/docker-entrypoint-initdb.d/data/model_input/$FILE' WITH (FORMAT CSV)"
    PGPASSWORD=$POSTGRESQL_PASSWORD psql -U $POSTGRESQL_USERNAME -d $POSTGRESQL_DATABASE -c "$COMMAND" &> /dev/null

    echo File: $FILE - import to table 'ethereum.model_input' successfully
done

# Import model_prediction data
for FILE in $(ls /docker-entrypoint-initdb.d/data/model_prediction)
do
    COMMAND="\copy ethereum.model_prediction FROM '/docker-entrypoint-initdb.d/data/model_prediction/$FILE' WITH (FORMAT CSV)"
    PGPASSWORD=$POSTGRESQL_PASSWORD psql -U $POSTGRESQL_USERNAME -d $POSTGRESQL_DATABASE -c "$COMMAND" &> /dev/null

    echo File: $FILE - import to table 'ethereum.model_prediction' successfully
done