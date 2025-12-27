from sqlalchemy.orm import Session
from .models import Tender

def seed_data(db: Session):
    if db.query(Tender).count() == 0:
        db.add_all([
            Tender(
                gem_id="GEM/2024/001",
                title="Supply of Electrical Cables",
                department="Power Ministry",
                value=1200000,
                raw_text="Supply and installation of LT electrical cables",
                extracted="LT cable installation"
            ),
            Tender(
                gem_id="GEM/2024/002",
                title="IT Hardware Procurement",
                department="IT Ministry",
                value=2500000,
                raw_text="Procurement of laptops and servers",
                extracted="Laptop + Server procurement"
            ),
        ])
        db.commit()


def get_all_tenders(db: Session):
    return db.query(Tender).all()


def get_tender_by_id(db: Session, tender_id: int):
    return db.query(Tender).filter(Tender.id == tender_id).first()
