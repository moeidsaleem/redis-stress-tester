import redis
from config import redis_host, redis_port

# Connect to Redis
def get_redis_client():
    return redis.StrictRedis(host=redis_host, port=redis_port)