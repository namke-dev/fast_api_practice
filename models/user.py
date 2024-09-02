from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class UserModel(BaseModel):
    id: UUID
    company_id: UUID
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
    isActive: bool
    isAdmin: bool

class UserClaims(BaseModel):
    id: str
    isActive: bool
    isAdmin: bool
    
class SearchUserModel(BaseModel):
    username: str | None = None
    email: str | None = None
    is_active: bool | None = None
    page: int = 1
    size: int = 10

    class Config:
        orm_mode = True