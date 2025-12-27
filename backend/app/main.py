from fastapi import FastAPI
from .database import Base, engine, SessionLocal
from .models import Tender

app = FastAPI(title="GeM Bid Analyzer")

# Create tables
Base.metadata.create_all(bind=engine)

def seed_tenders():
    db = SessionLocal()
    if db.query(Tender).count() == 0:
        tenders = [
            Tender(
                title="Supply of Electrical Cables",
                description="Supply and installation of LT electrical cables",
                department="CPWD",
                value=2500000
            ),
            Tender(
                title="Road Repair Work",
                description="Resurfacing of highways",
                department="PWD",
                value=5200000
            )
        ]
        db.add_all(tenders)
        db.commit()
    db.close()

seed_tenders()

@app.get("/tenders")
def get_tenders():
    db = SessionLocal()
    return db.query(Tender).all()
