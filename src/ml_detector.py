import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, ".."))

model = joblib.load(os.path.join(PROJECT_DIR, "phishing_model.pkl"))
vectorizer = joblib.load(os.path.join(PROJECT_DIR, "vectorizer.pkl"))

def ml_detect(url):
    X = vectorizer.transform([url])
    prediction = model.predict(X)
    return prediction[0] == 1
