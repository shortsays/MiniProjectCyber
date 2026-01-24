from url_analyzer import is_suspicious

def analyze_http(host, path):
    url = f"{host}{path}"
    if is_suspicious(url):
        return True, url
    return False, url
