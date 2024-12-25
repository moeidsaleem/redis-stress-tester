# Redis Overload Testing

This project is designed to test the performance and stability of a Redis server by inserting keys until a specified memory limit is reached. It supports parallel execution to maximize the load on the server.

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd overload-redis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**
   - Create a `.env` file in the root directory with the following content:
     ```
     REDIS_HOST=<your-redis-host>
     REDIS_PORT=<your-redis-port>
     ```

4. **Run the project**
   ```bash
   python3 main.py
   ```

## Configuration

- Adjust the settings in `config.py` to change the memory limit, key prefix, value size, report interval, and number of threads.

## Error Handling

- The script handles Redis server crashes and will print a message if the server becomes unreachable.

## Author

- **Moeid Saleem Khan**
  - GitHub: [moeidsaleem](https://github.com/moeidsaleem)
  - Email: moeid@atrix.digital

For project requirements or inquiries, feel free to reach out.

## License

This project is licensed under the MIT License.