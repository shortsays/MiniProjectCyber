def is_suspicious(url):
    suspicious_keywords = [
        "login", "verify", "bank", "secure",
        "account", "update", "free", "bonus"
    ]

    if len(url) > 50:
        return True

    for word in suspicious_keywords:
        if word in url.lower():
            return True

    import re
    if re.search(r'(\d{1,3}\.){3}\d{1,3}', url):
        return True

    return False