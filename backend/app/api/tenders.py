from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Tender

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
def list_tenders(db: Session = Depends(get_db)):
    return db.query(Tender).all()


@router.get("/{tender_id}")
def get_tender(tender_id: int, db: Session = Depends(get_db)):
    return db.query(Tender).filter(Tender.id == tender_id).first()
