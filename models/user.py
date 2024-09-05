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
    username: Optional[str] = None
    company_id: Optional[UUID] = None
    page: int = 1
    size: int = 10
        
class UserCreateModel(BaseModel):
    username: str
    company_id: UUID
    email: Optional[str]
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True
        
        
class UserViewModel(BaseModel):
    id: UUID
    username: str
    company_id: UUID
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    is_active: bool
    is_admin: bool

    class Config:
        orm_mode = True
        
class UserUpdateModel(BaseModel):
    company_id: UUID
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    password: str
    is_active: bool
    is_admin: bool