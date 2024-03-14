#!/usr/bin/env bash

echo "Start database migration..."
airflow db migrate

echo "Start database upgrade..."
airflow db upgrade

echo "Creating admin user..."
airflow users create -r Admin -u admin -e airflow@test.com -p admin -f test -l test

echo "Start services..."
airflow scheduler & \
    airflow webserver