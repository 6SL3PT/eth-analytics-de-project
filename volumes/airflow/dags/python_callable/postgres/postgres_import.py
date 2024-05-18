import logging
import os
import psycopg2

from datetime import date, timedelta


def run_postgres_import():
    try:
        # Connect to PostgreSQL
        logging.info('Connecting to database...')
        conn = psycopg2.connect(dbname='postgres', user='postgres', 
                                password='postgres', host='postgres')
        curr = conn.cursor()

        yesterday = date.today() - timedelta(days=1)

        # Import transactions data
        tx_temp_file = f'/opt/airflow/dags/python_callable/bigquery/temp_tx_{yesterday}.csv'
        assert os.path.exists(tx_temp_file)

        logging.info(f'Start import file \'{tx_temp_file}\' to table \'ethereum.transactions\' ...')
        with open(tx_temp_file, 'r') as f:
            curr.copy_expert('COPY ethereum.transactions FROM stdin WITH CSV', file=f)
        logging.info('Successfully import `transactions` data')

        # Commit import
        conn.commit()
        logging.info('Successfully commit import')

        # Remove temp file
        os.remove(tx_temp_file)
        logging.info(f'Delete temp file \'{tx_temp_file}\'')
        
    except (Exception, psycopg2.DatabaseError) as err:
        logging.error('Error in transaction, reverting all changes using rollback ', err)
        conn.rollback()
        raise err

    finally:
        if conn:
            curr.close()
            conn.close()