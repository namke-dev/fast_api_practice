from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class TaskModel(BaseModel):
    id: UUID
    summary: str
    description: Optional[str]
    status: str
    priority: int