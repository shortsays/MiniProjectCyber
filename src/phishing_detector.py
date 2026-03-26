from packet_sniffer import start_sniffing
from url_analyzer import is_suspicious
from ml_detector import ml_detect
from database import init_db, insert_log
import datetime
import os

init_db()

LOG_FILE = os.path.join(os.path.dirname(__file__), "../logs/detected_phishing.log")

seen_urls = set()


def clean_url(url):
    return url.strip().replace("\n", "").replace("\r", "")


def normalize_url(url):
  
    if not url.startswith("http"):
        return "http://" + url
    return url


def log_detection(source, url, confidence):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

   
    with open(LOG_FILE, "a") as f:
        f.write(
            f"[{datetime.datetime.now().strftime('%H:%M:%S')}] "
            f"{source} | {url} | {confidence:.2f}\n"
        )

    
    insert_log(
        datetime.datetime.now().strftime("%H:%M:%S"),
        source,
        url,
        confidence
    )


def detect(source, url):
    url = clean_url(url)

    # Remove duplicates
    if url in seen_urls:
        return
    seen_urls.add(url)

   
    ignore_list = ["microsoft", "azure", "github", "whatsapp", "digicert"]
    if any(x in url.lower() for x in ignore_list):
        return

    
    normalized_url = normalize_url(url)

    prediction, confidence = ml_detect(normalized_url)
    suspicious = is_suspicious(normalized_url)

    print(f"[CHECK] {source} | {url} → {confidence:.2f}")

    if (suspicious and confidence > 0.5) or (prediction == 1 and confidence > 0.7):

        print("\n🚨 PHISHING ALERT 🚨")
        print(f"URL       : {url}")
        print(f"Source    : {source}")
        print(f"Confidence: {confidence:.2f}")
        print("━━━━━━━━━━━━━━━━━━━━━━\n")

        log_detection(source, url, confidence)


if __name__ == "__main__":
    print("🛡️ Phishing Detection Started...\n")

    
    detect("TEST", "http://login-paypal-secure.com")
    detect("TEST", "secure-update-login.com")

    print("\n🔄 Listening for live traffic (DNS + HTTP + HTTPS)...\n")

    start_sniffing(detect)