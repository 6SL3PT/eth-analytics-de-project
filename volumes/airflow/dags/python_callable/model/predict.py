import joblib
import logging
import psycopg2

from datetime import date


def run_model_predict() -> None:
    import numpy as np
    import tensorflow as tf

    try:
        # Load model
        logging.info('Loading predictive model...')
        model = tf.keras.models.load_model(
            '/opt/airflow/dags/python_callable/model/keras_model/predictive_model.h5')

        # Load input scaler
        logging.info('Loading input scaler...')
        input_scaler = joblib.load(
            '/opt/airflow/dags/python_callable/model/scaler/input_scaler.pkl')
        
        db_conn_dict = {'dbname': 'postgres', 'user': 'postgres', 
                        'password': 'postgres', 'host': 'postgres'}

        # Fetch model input data
        SELECT = (
            '''
            SELECT volume_usd,
                tx_count,
                senkou_span_sub,
                alligator_sub
            FROM ethereum.model_input
            ORDER BY block_timestamp DESC
            LIMIT 30
            '''
        )
        logging.info(f'Fetching data for {date.today()} prediction...')
        with psycopg2.connect(**db_conn_dict) as conn:
            with conn.cursor() as curs:
                curs.execute(SELECT)
                query_result = curs.fetchall()
        
        model_input = input_scaler.transform(np.array(query_result)[::-1])
        model_input = np.array([[model_input]]).reshape(1, model_input.shape[1], 30, 1)
        
        # Predict
        logging.info(f'Predicting ISI Index of date \'{date.today()}\'...')
        result = model.predict(model_input).squeeze()
        logging.info(f'Today ISI Index is \'{result}\'')

        # Insert prediction result
        INSERT = (
            f'''
            INSERT INTO ethereum.model_prediction (
                block_timestamp, predict_result
            ) SELECT current_date::timestamptz,
                {result[0]};
            '''
        )
        logging.info(f'Inserting prediction result into model_prediction...')
        with psycopg2.connect(**db_conn_dict) as conn:
            with conn.cursor() as curs:
                curs.execute(INSERT)
                logging.info(f'Insert successfully')

    except (Exception, psycopg2.DatabaseError) as err:
        logging.error('Error in transaction, reverting all changes using rollback ', err)
        raise err
