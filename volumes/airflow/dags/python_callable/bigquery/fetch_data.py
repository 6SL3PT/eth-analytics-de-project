import glob
import os
import logging

from datetime import date, timedelta
from google.api_core.exceptions import Forbidden
from python_callable.bigquery.big_query_util import BigQuery, QueryError


def run_fetch_transaction():

    bq = BigQuery(wait_time=300)

    service_account_files = glob.glob(os.path.join('/opt/airflow/dags/python_callable/bigquery/service_account', 
                                                   '*.json'))
    assert len(service_account_files) > 0

    for file in service_account_files:
        client = bq.use_service_account(file)

        try:
            bq.check_tx_modified_time(client)
            break
        except QueryError as e:
            logging.error(e)
            raise e
        except Forbidden as e:
            logging.warning(f'Service account file \'{file}\' quota exceeded')

    assert os.path.exists(
        f'/opt/airflow/dags/python_callable/bigquery/temp_tx_{date.today() - timedelta(days=1)}.csv')
