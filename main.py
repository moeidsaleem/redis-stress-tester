from config import memory_limit_mb, key_prefix, value_size, report_interval, num_threads
from redis_connection import get_redis_client
from utils import generate_random_value, get_used_memory_mb
import time
import threading
import redis

client = get_redis_client()


def insert_keys():
    initial_memory = get_used_memory_mb()
    print(f'Initial memory usage: {initial_memory:.2f} MB')

    key_count = 0
    try:
        while True:
            current_memory = get_used_memory_mb()
            if current_memory - initial_memory >= memory_limit_mb:
                print(f'Memory limit of {memory_limit_mb} MB reached.')
                break

            key = f'{key_prefix}{key_count}'
            value = generate_random_value(value_size)
            client.set(key, value)
            key_count += 1

            if key_count % report_interval == 0:
                print(f'Inserted {key_count} keys. Current memory usage: {current_memory:.2f} MB')

            # Optional: Sleep to control the rate of inserts
            time.sleep(0.01)

    except redis.exceptions.ConnectionError:
        print('Redis server crashed or is unreachable.')

    except KeyboardInterrupt:
        print('Process interrupted by user.')

    finally:
        final_memory = get_used_memory_mb()
        print(f'Final memory usage: {final_memory:.2f} MB')
        print(f'Total keys inserted: {key_count}')


def main():
    threads = []
    for _ in range(num_threads):  # Use the number of threads from config
        thread = threading.Thread(target=insert_keys)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
