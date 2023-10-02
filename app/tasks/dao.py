from sqlalchemy import select

from app.database import async_session_maker
from app.dao.base import BaseDAO
from app.tasks.models import Tasks


class TaskDAO(BaseDAO):
    model = Tasks

    @classmethod
    async def add(cls):
        pass