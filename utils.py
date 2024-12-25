import random
import string
from redis_connection import get_redis_client

client = get_redis_client()


def generate_random_value(size):
    """Generate a random string of specified size."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=size))


def get_used_memory_mb():
    """Get the used memory in megabytes."""
    info = client.info('memory')
    return info.get('used_memory', 0) / (1024 * 1024) 