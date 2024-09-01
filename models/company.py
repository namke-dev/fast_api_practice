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