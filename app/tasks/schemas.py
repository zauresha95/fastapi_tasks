import re
from datetime import datetime, date
from pydantic import BaseModel, validator


class STasks(BaseModel):
    task_id: int
    category: str
    name: str
    time_to_do: str
    priority: str
    repeat: str
    # created: date = datetime.now()
    # updated: date = datetime.now()

    class Config:
        from_attributes = True


class STasksStatus(BaseModel):
    task_id: int
    status: str
    created: date = datetime.now()
    updated: date = datetime.now()

    class Config:
        from_attributes = True