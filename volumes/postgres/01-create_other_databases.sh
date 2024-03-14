#!/bin/bash

set -e
set -u

function create_user_and_database() {
	local database=$1
	echo "  Creating user and database '$database'"
    PGPASSWORD=$POSTGRESQL_PASSWORD \
		psql --echo-all -U $POSTGRESQL_USERNAME -c "CREATE USER $database WITH PASSWORD '$database'" &> /dev/null
	PGPASSWORD=$POSTGRESQL_PASSWORD \
		psql --echo-all -U $POSTGRESQL_USERNAME -c "CREATE DATABASE $database OWNER $database" &> /dev/null
	PGPASSWORD=$POSTGRESQL_PASSWORD \
		psql --echo-all -U $POSTGRESQL_USERNAME -c "GRANT ALL PRIVILEGES ON DATABASE $database TO $database" &> /dev/null
}

if [ -n "$POSTGRESQL_OTHER_DATABASES" ]; then
	echo "Multiple database creation requested: $POSTGRESQL_OTHER_DATABASES"
	for db in $(echo $POSTGRESQL_OTHER_DATABASES | tr ',' ' '); do
		create_user_and_database $db
	done
fi