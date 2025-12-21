from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import Base, engine, SessionLocal
from .api import tenders
from .models import Tender

app = FastAPI(title="GeM Bid Analyser API")

# ----------------------------
# CORS (required for frontend)
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # OK for MVP
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# Database setup
# ----------------------------
Base.metadata.create_all(bind=engine)

# ----------------------------
# Seed sample data (ONLY if empty)
# ----------------------------
def seed_tenders():
    db = SessionLocal()
    try:
        count = db.query(Tender).count()
        if count == 0:
            db.add_all([
                Tender(
                    title="Supply of Electrical Cables",
                    description="Supply and installation of LT electrical cables",
                    department="CPWD"
                ),
                Tender(
                    title="IT Hardware Procurement",
                    description="Procurement of laptops and peripherals",
                    department="Ministry of IT"
                ),
                Tender(
                    title="Security Services Contract",
                    description="Outsourcing of security guards",
                    department="Railways"
                )
            ])
            db.commit()
    finally:
        db.close()

seed_tenders()

# ----------------------------
# Routes
# ----------------------------
app.include_router(
    tenders.router,
    prefix="/api/tenders",
    tags=["tenders"]
)

@app.get("/health")
def health():
    return {"status": "ok"}
