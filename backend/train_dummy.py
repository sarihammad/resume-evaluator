from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

X = [
    "Experience with Python, SQL, Pandas, and data modeling.",
    "Developed deep learning models using TensorFlow and PyTorch.",
    "Built ETL pipelines and deployed APIs using Flask and Docker.",
    "Created dashboards in Excel, worked with large datasets.",
    "Wrote REST APIs with FastAPI, deployed to AWS ECS.",
    "Developed microservices using Java and Spring Boot.",
    "Created Tableau dashboards and ran SQL analytics."
]

y = [
    "Data Analyst",
    "Machine Learning Engineer",
    "Backend Engineer",
    "Data Analyst",
    "Backend Engineer",
    "Software Engineer",
    "Data Analyst"
]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

model.fit(X, y)
joblib.dump(model, "model/resume_model.pkl")
