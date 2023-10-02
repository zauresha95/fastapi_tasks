import asyncio

from fastapi import APIRouter
import sys
from os.path import abspath, dirname
from fastapi_cache.decorator import cache
from sqlalchemy import select

sys.path.insert(0, dirname(dirname(dirname(abspath(__file__)))))

# from app.database import async_session_maker
from app.tasks.schemas import STasks
from app.tasks.dao import TaskDAO


router = APIRouter(
    prefix="/tasks",
    tags=['Tasks'],
)


# @router.get("", response_model=None)
# @router.get("")
# @cache(expire=20)
# async def get_tasks() -> list[dict[str, STasks]]:
#     await asyncio.sleep(3)
#     return await TaskDAO.find_all()

#
# @router.get("")
# async def get_tasks_by_id():
#     return await TaskDAO.find_by_id(1)


# @router.get("")
# async def get_tasks_one_or_none():
#     return await TaskDAO.find_one_or_none()