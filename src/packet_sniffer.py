from scapy.all import sniff, DNSQR, TCP, Raw
from url_analyzer import is_suspicious
from http_analyzer import analyze_http
from ml_detector import ml_detect
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(BASE_DIR, "..", "logs")
LOG_FILE = os.path.join(LOG_DIR, "detected_phishing.log")

os.makedirs(LOG_DIR, exist_ok=True)

def log_alert(source, value):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} - {source}: {value}\n")

def process_packet(packet):

    # 🔹 DNS Detection
    if packet.haslayer(DNSQR):
        domain = packet[DNSQR].qname.decode(errors="ignore").strip(".")

        if is_suspicious(domain) or ml_detect(domain):
            print(f"[DNS ALERT] Phishing Domain: {domain}")
            log_alert("DNS", domain)

    # 🔹 HTTP Detection
    if packet.haslayer(TCP) and packet.haslayer(Raw):
        payload = packet[Raw].load.decode(errors="ignore")

        if payload.startswith("GET") or payload.startswith("POST"):
            lines = payload.split("\r\n")
            host = ""
            path = payload.split(" ")[1]

            for line in lines:
                if line.startswith("Host:"):
                    host = line.split(" ")[1]

            if host:
                detected, url = analyze_http(host, path)
                if detected or ml_detect(url):
                    print(f"[HTTP ALERT] Phishing URL: {url}")
                    log_alert("HTTP", url)

def start_sniffing():
    sniff(filter="udp port 53 or tcp port 80", prn=process_packet, store=0)
