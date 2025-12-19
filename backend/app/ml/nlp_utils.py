import re
try:
    import spacy
    nlp = spacy.load('en_core_web_sm')
except Exception:
    nlp = None

CERT_PATTERNS = [
    r"ISO\s*9001",
    r"GSTIN",
    r"MSME",
    r"turnover\s*of\s*([₹\d,]+)",
]

def extract_eligibility(text: str) -> dict:
    out = {'certificates': [], 'turnover': None, 'other': []}
    for p in CERT_PATTERNS:
        m = re.search(p, text, flags=re.I)
        if m:
            out['certificates'].append(m.group(0))
            if 'turnover' in p and m.groups():
                out['turnover'] = m.group(1)
    if nlp:
        doc = nlp(text)
        for ent in doc.ents:
            if ent.label_ == 'MONEY':
                out['other'].append({'money_entity': ent.text})
    return out
