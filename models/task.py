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
    
class TaskViewModel(BaseModel):
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

class TaskCreateModel(BaseModel):
    summary: str
    description: Optional[str] = None
    status: str
    user_id: UUID

class TaskUpdateModel(BaseModel):
    summary: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[int] = None
    