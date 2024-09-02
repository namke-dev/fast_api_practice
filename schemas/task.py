from uuid import UUID as UUIDType
from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(pgUUID(as_uuid=True), primary_key=True, nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    owner_id = Column(pgUUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    is_complete = Column(Boolean, default=False, nullable=False)
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

