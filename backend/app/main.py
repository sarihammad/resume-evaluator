from fastapi import FastAPI, UploadFile, File
from app.model.predict import predict_resume
from app.utils.extract_text import extract_text_from_file
from app.schemas import PredictionResponse

app = FastAPI()

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_file(content, file.filename)
    result = predict_resume(text)
    return result
