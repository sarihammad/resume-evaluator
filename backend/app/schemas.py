from pydantic import BaseModel
from typing import List

class PredictionResponse(BaseModel):
    predicted_title: str
    confidence: float
    skills: List[str]
