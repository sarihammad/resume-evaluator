import joblib
from pathlib import Path
from app.utils.extract_skills import extract_skills

model_path = Path("model/resume_model.pkl")
model = joblib.load(model_path)

def predict_resume(text: str):
    prediction = model.predict([text])[0]
    confidence = max(model.predict_proba([text])[0])
    skills = extract_skills(text)
    return {
        "predicted_title": prediction,
        "confidence": round(confidence, 3),
        "skills": skills
    }
