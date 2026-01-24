from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import joblib

urls = [
    "secure-login-update.com",
    "verify-bank-account.net",
    "free-gift-card.com",
    "signin-paypal-alert.com",
    "google.com",
    "github.com",
    "openai.com",
    "microsoft.com"
]

labels = [1, 1, 1, 1, 0, 0, 0, 0]  # 1 = phishing, 0 = safe

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(urls)

model = RandomForestClassifier()
model.fit(X, labels)

joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("ML model trained and saved successfully.")
