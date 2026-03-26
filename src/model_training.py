import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from feature_extractor import extract_features
import joblib
import os

data = pd.read_csv("../dataset.csv")

urls = data['url']
labels = data['label']

X = [extract_features(url) for url in urls]
y = labels

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=200)
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

os.makedirs("../models", exist_ok=True)
joblib.dump(model, "../models/phishing_model.pkl")

print("✅ Model trained and saved!")