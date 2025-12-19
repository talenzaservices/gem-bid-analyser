from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TenderBase(BaseModel):
    title: str
    department: Optional[str]
    value: Optional[float]
    raw_text: str

class TenderCreate(TenderBase):
    gem_id: Optional[str]

class Tender(TenderBase):
    id: int
    score: float
    extracted: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: str
    name: Optional[str]
    password: str

class UserOut(BaseModel):
    id: int
    email: str
    name: Optional[str]
    class Config:
        orm_mode = True
