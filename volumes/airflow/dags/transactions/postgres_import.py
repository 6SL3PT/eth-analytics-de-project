import logging
import os
import psycopg2

from datetime import date, timedelta


def run_postgres_import():
    try:
        logging.info('Connecting to database...')
        conn = psycopg2.connect(dbname='postgres', user='postgres', 
                                password='postgres', host='postgres')
        curr = conn.cursor()

        yesterday = date.today() - timedelta(days=1)

        temp_file = f'/opt/airflow/dags/transactions/temp_{yesterday}.csv'
        assert os.path.exists(temp_file)

        logging.info(f'Start import file \'{temp_file}\' to table \'ethereum.transactions\' ...')
        with open(temp_file, 'r') as f:
            curr.copy_expert('COPY ethereum.transactions FROM stdin WITH CSV', file=f)

        conn.commit()
        logging.info('Successfully finished the transaction')

        os.remove(temp_file)
        logging.info(f'Delete temp file \'{temp_file}\'')
        
    except (Exception, psycopg2.DatabaseError) as err:
        logging.error('Error in transaction, reverting all changes using rollback ', err)
        conn.rollback()

    finally:
        if conn:
            curr.close()
            conn.close()