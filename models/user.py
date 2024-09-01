from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class UserModel(BaseModel):
    id: UUID
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
    isActive: bool
    isAdmin: bool
