import requests
from bs4 import BeautifulSoup
from ..schemas import TenderCreate
from ..crud import create_tender
from ..db import SessionLocal

def fetch_and_store_sample(url: str):
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find('h1') and soup.find('h1').get_text(strip=True) or 'Untitled'
    body = '\n'.join([p.get_text(strip=True) for p in soup.find_all('p')])
    db = SessionLocal()
    try:
        tc = TenderCreate(title=title, department=None, value=None, raw_text=body)
        t = create_tender(db, tc)
        print('Saved tender id', t.id)
    finally:
        db.close()

if __name__ == '__main__':
    sample_url = 'https://example.com/sample-tender-page'
    fetch_and_store_sample(sample_url)
