from fastapi import APIRouter, Depends
from ..dependencies import fixed_rate_limit, sliding_log_rate_limit

router = APIRouter()

@router.get("/fixed-limited", dependencies=[Depends(fixed_rate_limit)])
async def get_fixed_limited_resource():
    """
    An endpoint protected by the Fixed Window rate limiter.
    Allows 5 requests per 10 seconds per client.
    """
    return {"message": "You accessed the fixed-window limited resource!"}

@router.get("/sliding-limited", dependencies=[Depends(sliding_log_rate_limit)])
async def get_sliding_limited_resource():
    """
    An endpoint protected by the Sliding Window Log rate limiter.
    Allows 3 requests per 60 seconds per client.
    """
    return {"message": "You accessed the sliding-window-log limited resource!"}