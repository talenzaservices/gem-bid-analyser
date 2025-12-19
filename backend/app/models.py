from sqlalchemy import Column, Integer, String, Text, DateTime, Float, Boolean
from sqlalchemy.sql import func
from .db import Base

class Tender(Base):
    __tablename__ = 'tenders'
    id = Column(Integer, primary_key=True, index=True)
    gem_id = Column(String, unique=True, index=True, nullable=True)
    title = Column(String, index=True)
    department = Column(String, index=True)
    value = Column(Float, nullable=True)
    raw_text = Column(Text)
    extracted = Column(Text)
    score = Column(Float, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    name = Column(String)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)
