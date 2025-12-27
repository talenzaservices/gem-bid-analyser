from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Tender(Base):
    __tablename__ = "tenders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    department = Column(String, nullable=False)
    value = Column(Float, nullable=False)
