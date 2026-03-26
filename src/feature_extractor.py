def extract_features(url):
    try:
        features = []

        features.append(len(url))
        features.append(url.count('.'))
        features.append(url.count('-'))
        features.append(1 if "https" in url else 0)

        import re
        ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
        features.append(1 if re.search(ip_pattern, url) else 0)

        features.append(sum(c.isdigit() for c in url))
        features.append(sum(not c.isalnum() for c in url))

        return features

    except:
        return [0]*7