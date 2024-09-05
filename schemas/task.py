import uuid
from uuid import UUID as UUIDType
from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime, SmallInteger
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    summary = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=True)
    user_id = Column(UUID(as_uuid=True))
    priority = Column(SmallInteger, nullable=True)
