import joblib
from feature_extractor import extract_features
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/phishing_model.pkl")
model = joblib.load(MODEL_PATH)

def ml_detect(url):
    try:
        features = extract_features(url)

        prediction = model.predict([features])[0]
        probability = model.predict_proba([features])[0][1]

        return prediction, probability

    except:
        return 0, 0.0