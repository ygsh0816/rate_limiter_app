sliding_log_lua_script = """
local key = KEYS[1]
local current_time = tonumber(ARGV[1])
local window_size = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])

-- Remove timestamps older than the window size
redis.call("ZREMRANGEBYSCORE", key, 0, current_time - window_size)

-- Check the number of requests in the current window
local request_count = redis.call("ZCARD", key)

if request_count >= limit then
    return 0  -- Rate limit exceeded
end

-- Add the current request timestamp
redis.call("ZADD", key, current_time, current_time)

-- Set expiration for the key
redis.call("EXPIRE", key, window_size)

return 1  -- Request allowed
"""


fixed_rate_lua_script = """
local key = KEYS[1]
local window_size = tonumber(ARGV[1])
local limit = tonumber(ARGV[2])

-- Get the current request count
local request_count = redis.call("GET", key)

if request_count then
    request_count = tonumber(request_count)
else
    request_count = 0
end

-- Check if the request count exceeds the limit
if request_count >= limit then
    return 0  -- Rate limit exceeded
end

-- Increment the request count and set expiration if it's the first request
request_count = redis.call("INCR", key)
if request_count == 1 then
    redis.call("EXPIRE", key, window_size)
end

return 1  -- Request allowed
"""