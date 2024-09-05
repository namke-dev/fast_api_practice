from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class CompanyModel(BaseModel):
    id: UUID
    name: str
    description: Optional[str]
    mode: str
    rating: int
    
    class Config:
        orm_mode = True
        
class CompanyViewModel(BaseModel):
    id: UUID
    name: str
    description: str | None
    mode: str
    rating: int

    class Config:
        orm_mode = True

class CompanyCreateModel(BaseModel):
    name: str
    description: str | None
    mode: str
    rating: int

    class Config:
        orm_mode = True
        

class SearchCompanyModel(BaseModel):
    name: str | None = None
    mode: str | None = None
    page: int = 1
    size: int = 10

    class Config:
        orm_mode = True