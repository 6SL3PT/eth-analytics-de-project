import os
import psycopg2

from custom_ethereumetl.cli.stream import stream
from datetime import date
from dotenv import load_dotenv
from requests.exceptions import HTTPError

def start_stream():
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres", 
                                password="postgres", host="postgres")
        curr = conn.cursor()
        curr.execute('SELECT block FROM ethereum.block_price ORDER BY block DESC LIMIT 1')

        last_synced_block = str(curr.fetchall()[0][0])
        with open('last_synced_block.txt', 'w') as f:
            f.write(last_synced_block)
        curr.close()
    except psycopg2.OperationalError as e:
        print('[ERROR] Fail to connect to database')
        return 0
    except Exception as e:
        print('[ERROR] Fail to write last_synced_block.txt')
        curr.close()
        return 0

    load_dotenv()
    api_keys = os.environ.get('API_KEYS')

    if api_keys is None: raise Exception('API_KEYS not found in .env file')

    api_key_list = api_keys.split(',')
    for api_key in api_key_list:
        try:
            provider_uri = 'https://mainnet.infura.io/v3/' + api_key
            stream(last_synced_block_file='/opt/ethereumetl/last_synced_block.txt',
                   provider_uri=provider_uri,
                   output='kafka/kafka:9092',
                   block_batch_size=1,
                   entity_types='block')
        except HTTPError as e:
            print(f'[ERROR] {e}')
        except Exception as e:
            raise e
    print('[WARNING] Out of available API key')

if __name__ == "__main__":
    start_stream()