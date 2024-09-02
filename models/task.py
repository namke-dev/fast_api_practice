from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class TaskModel(BaseModel):
    id: UUID
    user_id: UUID
    summary: str
    description: Optional[str]
    status: str
    priority: int
    
class SearchTaskModel(BaseModel):
    user_id: str | None = None
    status: str | None = None
    page: int = 1
    size: int = 10

    class Config:
        orm_mode = True

class TaskViewModel(BaseModel):
    id: UUID
    user_id: UUID
    status: str

    class Config:
        orm_mode = True
