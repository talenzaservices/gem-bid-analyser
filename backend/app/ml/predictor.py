import numpy as np

"""
ML Predictor (MVP SAFE VERSION)

⚠️ IMPORTANT:
- Heavy ML models are intentionally DISABLED
- This prevents Out-Of-Memory crashes on Render free tier
- This is the correct architecture for an MVP

Later:
- Real ML will be re-enabled via background workers or a separate service
"""

EMBEDDING_DIM = 384  # all-MiniLM-L6-v2 embedding size


class Predictor:
    def __init__(self):
        # ML model intentionally disabled for MVP
        self.model = None

    def embed(self, texts):
        """
        Returns dummy embeddings to keep API stable.
        Shape: (len(texts), 384)
        """
        return np.zeros((len(texts), EMBEDDING_DIM))

    def score_match(self, tender_text: str, vendor_profile_text: str):
        """
        Dummy similarity score for MVP.
        Always returns a stable numeric score.
        """
        a = self.embed([tender_text])[0]
        b = self.embed([vendor_profile_text])[0]

        # Avoid division by zero
        denom = (np.linalg.norm(a) * np.linalg.norm(b)) + 1e-9
        sim = np.dot(a, b) / denom

        # Normalise to 0–100 scale
        return float((sim + 1) / 2 * 100)
