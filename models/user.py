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
    id: UUID
    isActive: bool
    isAdmin: bool