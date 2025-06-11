import spacy
from pathlib import Path

nlp = spacy.load("en_core_web_sm")

skills_path = Path("app/data/skills.txt")
with open(skills_path, "r") as f:
    skill_keywords = set(skill.strip().lower() for skill in f.readlines())

def extract_skills(text: str):
    doc = nlp(text)
    extracted = set()

    for token in doc:
        if token.text.lower() in skill_keywords:
            extracted.add(token.text.lower())

    for chunk in doc.noun_chunks:
        if chunk.text.lower() in skill_keywords:
            extracted.add(chunk.text.lower())

    return sorted(extracted)
