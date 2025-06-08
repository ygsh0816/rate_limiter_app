# Rate Limiter Application

This project is a FastAPI application that implements rate limiting using Redis. It provides endpoints that demonstrate two different rate limiting strategies: Fixed Window and Sliding Window Log.

## Features

- **Fixed Window Rate Limiting**: Limits the number of requests a client can make in a specified time frame.
- **Sliding Window Log Rate Limiting**: Allows a more flexible rate limiting approach by tracking requests over time.

## Implementation Details

The rate-limiting logic is implemented in two ways:
1. **Using Lua Scripts**: Lua scripts are executed directly on the Redis server for atomic operations and better performance.
2. **Using Direct Redis Client Calls**: The logic is implemented in Python by calling Redis commands directly.

### Switching Between Implementations

The `main.py` file defines the endpoints and their dependencies. You can switch between the Lua script-based implementation and the direct Redis client implementation by updating the dependencies in the route definitions.

#### Example:

To use the **Lua script-based implementation**, update the dependencies as follows:
<pre>
from ..dependencies import fixed_rate_limit_with_lua_script, sliding_log_rate_limit_with_lua_script

@app.get("/fixed-limited", dependencies=[Depends(fixed_rate_limit_with_lua_script)])
async def get_fixed_limited_resource():
    return {"message": "You accessed the fixed-window limited resource!"}

@app.get("/sliding-limited", dependencies=[Depends(sliding_log_rate_limit_with_lua_script)])
async def get_sliding_limited_resource():
    return {"message": "You accessed the sliding-window-log limited resource!"}

</pre>

To use the **direct Redis client implementation**, update the dependencies as follows:
<pre>
from ..dependencies import fixed_rate_limit, sliding_log_rate_limit

@app.get("/fixed-limited", dependencies=[Depends(fixed_rate_limit)])
async def get_fixed_limited_resource():
    return {"message": "You accessed the fixed-window limited resource!"}

@app.get("/sliding-limited", dependencies=[Depends(sliding_log_rate_limit)])
async def get_sliding_limited_resource():
    return {"message": "You accessed the sliding-window-log limited resource!"}

</pre>


## Project Structure

```
rate_limiter   
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
uvicorn rate_limiter.app.main:app --host 0.0.0.0 --port 8000 --reload
```

The application will be accessible at `http://0.0.0.0:8000`.

## Endpoints

- **GET /**: A basic endpoint to check if the application is running.
- **GET /fixed-limited**: Access this endpoint to test the Fixed Window rate limiting.
- **GET /sliding-limited**: Access this endpoint to test the Sliding Window Log rate limiting.

## Running Tests

To run the unit tests for the rate limiting functionality, use:
```
pytest tests/test_rate_limiter.py
```

## Notes
The Lua script-based implementation is more efficient and ensures atomicity for rate-limiting logic.
The direct Redis client implementation is simpler but may involve multiple Redis calls, which could lead to race conditions in high-concurrency scenarios.
Ensure that Redis is running locally on localhost:6379 or update the configuration in config.py if needed.
