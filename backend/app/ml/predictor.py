from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = 'all-MiniLM-L6-v2'

class Predictor:
    def __init__(self):
        self.model = SentenceTransformer(MODEL_NAME)

    def embed(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)

    def score_match(self, tender_text: str, vendor_profile_text: str):
        a = self.embed([tender_text])[0]
        b = self.embed([vendor_profile_text])[0]
        sim = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-9)
        return float((sim + 1) / 2 * 100)
