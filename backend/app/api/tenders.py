from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..db import get_db
from ..ml.predictor import Predictor
from ..ml.nlp_utils import extract_eligibility

router = APIRouter()
predictor = Predictor()

@router.post('/', response_model=schemas.Tender)
def create_tender(t: schemas.TenderCreate, db: Session = Depends(get_db)):
    db_t = crud.create_tender(db, t)
    extracted = extract_eligibility(db_t.raw_text)
    vendor_profile = "MSME registered, ISO 9001, turnover ₹50,00,000"
    score = predictor.score_match(db_t.raw_text, vendor_profile)
    crud.update_tender_score(db, db_t.id, score, extracted)
    return db_t

@router.get('/', response_model=list[schemas.Tender])
def list_tenders(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return crud.get_tenders(db, skip, limit)
