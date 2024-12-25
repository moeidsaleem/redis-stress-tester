# Configuration
redis_host = '20.74.202.75'  # Replace with your Redis host
redis_port = 6379         # Replace with your Redis port
memory_limit_mb = 2000000     # Memory limit in megabytes for the test (2 GB)
key_prefix = 'test_key_'  # Prefix for the keys to avoid collision with existing data
value_size = 4096         # Size of each value in bytes (4 KB)
report_interval = 500     # Report status more frequently (every 500 inserts)
num_threads = 50  # Number of threads for parallel execution