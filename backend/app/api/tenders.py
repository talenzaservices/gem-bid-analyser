from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Tender

router = APIRouter()

# =====================================================
# MVP VERSION — ML DISABLED COMPLETELY
# No Predictor import
# No numpy
# No ML usage
# =====================================================


@router.get("/", summary="List tenders")
def list_tenders(db: Session = Depends(get_db)):
    tenders = db.query(Tender).all()
    return [
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "estimated_value": t.estimated_value,
            "match_score": 50.0,  # Static MVP score
        }
        for t in tenders
    ]


@router.get("/{tender_id}", summary="Get tender details")
def get_tender(tender_id: int, db: Session = Depends(get_db)):
    tender = db.query(Tender).filter(Tender.id == tender_id).first()

    if not tender:
        return {"error": "Tender not found"}

    return {
        "id": tender.id,
        "title": tender.title,
        "description": tender.description,
        "estimated_value": tender.estimated_value,
        "match_score": 50.0,  # Static MVP score
    }
