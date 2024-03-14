import json
import re
import subprocess
import time

import psycopg2
import confluent_kafka

def delivery_report(err, msg):
   if err:
      print(f'Message delivery failed: {err}')

def push_to_kafka(event, topic):
    producer = confluent_kafka.Producer({'bootstrap.servers': 'kafka:9092'})
    producer.produce(topic, json.dumps(event).encode('utf-8'), callback=delivery_report)
    producer.flush()

def start_fetch_price() -> None:
    conn = psycopg2.connect(dbname="postgres",
                            user="postgres",
                            password="postgres",
                            host="postgres")
    curr = conn.cursor()
    curr.execute('SELECT block FROM ethereum.block_price ORDER BY block DESC LIMIT 1')

    fetch_block = int(curr.fetchall()[0][0])
    fetch_block += 1
    success_fetch_chain = 0
    max_wait = 10
    wait_time = max_wait
    
    curr.close()
    print(f'START AT BLOCK: {fetch_block}')

    while True:
        command = f'0xweb contract read chainlink/oracle-eth latestAnswer --block {fetch_block}'
        result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

        try:
            block_price = {
                'block': fetch_block,
                'price': re.findall("[0-9]+n", str(result.stdout.read()))[0]
            }
            push_to_kafka(block_price, 'prices')
            print(f'FETCH_BLOCK: {fetch_block} - SUCCESS')

            fetch_block += 1
            success_fetch_chain += 1

            if wait_time > 0:
                time.sleep(wait_time)
            if success_fetch_chain > 3:
                wait_time -= (success_fetch_chain - 3) // 3

        except Exception as e:
            if isinstance(e, IndexError):
                print(f'FETCH_BLOCK: {fetch_block} - BLOCK_NOT_FOUND')
            elif isinstance(e, (confluent_kafka.KafkaException, confluent_kafka.KafkaError)):
                print(f'FETCH_BLOCK: {fetch_block} - KAFKA_ERROR')
            else:
                print(f'FETCH_BLOCK: {fetch_block} - UNKNOWN_ERROR')

            if wait_time == max_wait:
                time.sleep(5)
            else:
                time.sleep(10)
            
            success_fetch_chain = 0
            wait_time = max_wait

if __name__ == '__main__':
    start_fetch_price()
