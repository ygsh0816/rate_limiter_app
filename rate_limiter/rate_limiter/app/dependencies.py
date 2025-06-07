from fastapi import Request, HTTPException
from redis import Redis
import time

# Initialize Redis client
redis_client = Redis(host='localhost', port=6379, db=0)

def fixed_rate_limit(request: Request):
    client_ip = request.client.host
    current_time = int(time.time())
    window_size = 10  # 10 seconds
    limit = 5  # 5 requests

    # Create a unique key for the client
    key = f"fixed_rate_limit:{client_ip}:{current_time // window_size}"

    # Increment the request count
    request_count = redis_client.incr(key)

    # Set expiration for the key if it's the first request
    if request_count == 1:
        redis_client.expire(key, window_size)

    if request_count > limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")

def sliding_log_rate_limit(request: Request):
    client_ip = request.client.host
    current_time = int(time.time())
    window_size = 60  # 60 seconds
    limit = 3  # 3 requests

    # Create a unique key for the client
    key = f"sliding_log_rate_limit:{client_ip}"

    # Remove timestamps older than the window size
    redis_client.zremrangebyscore(key, 0, current_time - window_size)

    # Add the current request timestamp
    redis_client.zadd(key, {current_time: current_time})

    # Set expiration for the key
    redis_client.expire(key, window_size)

    # Check the number of requests in the current window
    request_count = redis_client.zcard(key)

    if request_count > limit:
        raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")