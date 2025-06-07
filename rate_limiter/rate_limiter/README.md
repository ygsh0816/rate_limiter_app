# Rate Limiter Application

This project is a FastAPI application that implements rate limiting using Redis. It provides endpoints that demonstrate two different rate limiting strategies: Fixed Window and Sliding Window Log.

## Features

- **Fixed Window Rate Limiting**: Limits the number of requests a client can make in a specified time frame.
- **Sliding Window Log Rate Limiting**: Allows a more flexible rate limiting approach by tracking requests over time.

## Project Structure

```
rate_limiter_app
├── app
│   ├── __init__.py
│   ├── main.py                # Entry point of the FastAPI application
│   ├── dependencies.py        # Rate limiting logic
│   ├── config.py             # Configuration settings and Redis client setup
│   └── routes
│       ├── __init__.py
│       └── rate_limiter_routes.py # Defines rate limiting routes
├── tests
│   ├── __init__.py
│   └── test_rate_limiter.py   # Unit tests for rate limiting functionality
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd rate_limiter_app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Ensure you have a Redis server running. You can use Docker to run Redis:
   ```
   docker run -d -p 6379:6379 redis
   ```

## Usage

To run the FastAPI application, execute the following command:
```
python -m app.main
```

The application will be accessible at `http://localhost:8000`.

## Endpoints

- **GET /**: A basic endpoint to check if the application is running.
- **GET /fixed-limited**: Access this endpoint to test the Fixed Window rate limiting.
- **GET /sliding-limited**: Access this endpoint to test the Sliding Window Log rate limiting.

## Running Tests

To run the unit tests for the rate limiting functionality, use:
```
pytest tests/test_rate_limiter.py
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.