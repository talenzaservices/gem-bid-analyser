from sqlalchemy.orm import Session
from . import models, schemas
import json

def create_tender(db: Session, tender: schemas.TenderCreate):
    db_t = models.Tender(
        gem_id=tender.gem_id,
        title=tender.title,
        department=tender.department,
        value=tender.value,
        raw_text=tender.raw_text,
    )
    db.add(db_t)
    db.commit()
    db.refresh(db_t)
    return db_t

def get_tenders(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Tender).order_by(models.Tender.created_at.desc()).offset(skip).limit(limit).all()

def update_tender_score(db: Session, tender_id: int, score: float, extracted: dict):
    t = db.query(models.Tender).get(tender_id)
    if not t:
        return None
    t.score = score
    t.extracted = json.dumps(extracted)
    db.commit()
    db.refresh(t)
    return t
