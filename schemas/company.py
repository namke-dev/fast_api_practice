# from uuid import UUID
import uuid
from sqlalchemy import Column, String, SmallInteger
from sqlalchemy.dialects.postgresql import UUID as pgUUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = 'companies'

    id = Column(pgUUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    description = Column(String, nullable=True)
    mode = Column(String(50), nullable=False)
    rating = Column(SmallInteger, nullable=False)
