from fastapi import FastAPI
from .db import Base, engine
from .api import tenders

app = FastAPI(title='GeM Bid Analyser API')
Base.metadata.create_all(bind=engine)
app.include_router(tenders.router, prefix='/api/tenders', tags=['tenders'])

@app.get('/health')
def health():
    return {'status': 'ok'}
