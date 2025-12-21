from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import Base, engine
from .api import tenders

# Create FastAPI app
app = FastAPI(
    title="GeM Bid Analyser API",
    version="0.1.0"
)

# ✅ CORS CONFIGURATION (CRITICAL)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",              # local frontend
        "http://127.0.0.1:5173",
        "https://gembid-frontend.onrender.com"  # future deployed frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(
    tenders.router,
    prefix="/api/tenders",
    tags=["tenders"]
)

# Health check
@app.get("/health")
def health():
    return {"status": "ok"}
