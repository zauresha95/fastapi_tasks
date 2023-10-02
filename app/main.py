from datetime import date
from fastapi import FastAPI, Query, Depends
from typing import Optional
from pydantic import BaseModel
import uvicorn
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
# from fastapi_versioning import VersionedFastAPI
# from prometheus_fastapi_instrumentator import Instrumentator
from redis import asyncio as aioredis

from tasks.schemas import STasks
from tasks.router import router as router_tasks
from app.config import settings
app = FastAPI()

app.include_router(router_tasks)

@app.on_event('startup')
def startup():
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix ='cache')

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)