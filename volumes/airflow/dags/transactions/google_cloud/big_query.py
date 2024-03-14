import logging
import time

from datetime import date, timedelta
from google.cloud.bigquery import Client
from google.oauth2 import service_account

class QueryError(Exception):
    pass

class BigQuery():

    def __init__(self, max_period_second: int):
        self.max_period_second = max_period_second
        self.yesterday = date.today() - timedelta(days=1)

    def use_service_account(self, key_path: str) -> Client:
        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )

        client = Client(credentials=credentials, project=credentials.project_id)
        logging.info(f'Using service account file \'{key_path}\'')

        return client

    def check_modified_time(self, client: Client) -> None:
        QUERY = (
            '''
            SELECT last_modified_time FROM `bigquery-public-data.crypto_ethereum.__TABLES__`
            WHERE table_id = 'transactions'
            '''
        )

        while True:
            result_df = client.query(QUERY).result().to_dataframe()
            modified_time = int(result_df['last_modified_time'].iloc[0])

            if modified_time >= time.mktime(date.today().timetuple()):
                logging.info(f'Start fetching transactions of date \'{self.yesterday}\'')
                self.fetch_yesterday_data(client)
                break
            else:
                logging.info(
                    f'Modified timestamp not up to date. Sleeping for {self.max_period_second} seconds...')
                time.sleep(self.max_period_second)

    def fetch_yesterday_data(self, client: Client) -> None:
        QUERY = (
            f'''
            WITH MIN_TX AS (
                SELECT TIMESTAMP_TRUNC(block_timestamp, MINUTE) AS `block_timestamp`,
                    gas_price, receipt_gas_used,
                    value,
                    to_address, from_address
                FROM `bigquery-public-data.crypto_ethereum.transactions`
                WHERE CAST(block_timestamp AS DATE) = '{self.yesterday}'
            )
            SELECT 
                EXTRACT(YEAR FROM block_timestamp) ||
                    SUBSTR('0' || CAST(EXTRACT(MONTH FROM block_timestamp) AS STRING), -2) ||
                    SUBSTR('0' || CAST(EXTRACT(DAY FROM block_timestamp) AS STRING), -2) ||
                    SUBSTR('0' || CAST(EXTRACT(HOUR FROM block_timestamp) AS STRING), -2) ||
                    SUBSTR('0' || CAST(EXTRACT(MINUTE FROM block_timestamp) AS STRING), -2) 
                    AS `minute_group_id`,
                AGG.block_timestamp,
                avg_gas_price_gwei,
                tx_fees_eth,
                volume_eth,
                active_address
            FROM
                (
                    SELECT block_timestamp,
                    AVG(gas_price / POW(10,9)) AS `avg_gas_price_gwei`,
                    SUM(gas_price / POW(10,18) * receipt_gas_used) AS `tx_fees_eth`,
                    SUM(value / POW(10,18)) AS `volume_eth`
                    FROM MIN_TX
                    GROUP BY block_timestamp
                ) AGG
                LEFT JOIN
                (
                    SELECT block_timestamp, COUNT(DISTINCT address) AS `active_address`
                    FROM MIN_TX CROSS JOIN
                    UNNEST(ARRAY[from_address, to_address]) address
                    GROUP BY block_timestamp
                ) ADDRESS
                ON AGG.block_timestamp = ADDRESS.block_timestamp
            ORDER BY AGG.block_timestamp
            '''
        )
        result = client.query(QUERY).result()
        if result.total_rows is not None and result.total_rows > 0:
            result_df = result.to_dataframe()
            result_df.to_csv(
                f'/opt/airflow/dags/transactions/temp_{self.yesterday}.csv', index=False, header=False)
        else:
            raise QueryError(f'total result from query \'{result.total_rows}\'')
