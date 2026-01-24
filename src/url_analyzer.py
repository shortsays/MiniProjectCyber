import re

keywords = [
    "login", "secure", "bank", "verify", "account",
    "update", "free", "gift", "confirm", "signin"
]

def is_suspicious(text):
    text = text.lower()

    if len(text) > 35:
        return True

    for word in keywords:
        if word in text:
            return True

    if re.match(r"\d+\.\d+\.\d+\.\d+", text):
        return True

    return False
