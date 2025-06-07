from fastapi import FastAPI, Depends
from .dependencies import fixed_rate_limit, sliding_log_rate_limit
from .config import redis_client

app = FastAPI(title="Redis Rate Limiter Example")

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Rate Limiter Example!"}

@app.get("/fixed-limited", dependencies=[Depends(fixed_rate_limit)])
async def get_fixed_limited_resource():
    return {"message": "You accessed the fixed-window limited resource!"}

@app.get("/sliding-limited", dependencies=[Depends(sliding_log_rate_limit)])
async def get_sliding_limited_resource():
    return {"message": "You accessed the sliding-window-log limited resource!"}

@app.on_event("shutdown")
async def shutdown_event():
    if redis_client:
        print("Closing Redis connection pool...")
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)