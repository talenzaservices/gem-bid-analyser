from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import Base, engine
from .api import tenders

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="GeM Bid Analyser API",
    version="0.1.0"
)

# -----------------------------
# CORS (IMPORTANT)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",          # local frontend
        "https://gembid-backend-kj2a.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Routes
# -----------------------------
app.include_router(
    tenders.router,
    prefix="/api/tenders",
    tags=["tenders"]
)

@app.get("/health")
def health():
    return {"status": "ok"}
