# 🛡️ Network-Based Phishing Detection Tool

A real-time **network-based phishing detection system** that analyzes **DNS and HTTP traffic** to identify phishing attempts using **rule-based techniques and machine learning**.

---

## 📌 Introduction

Phishing is one of the most common cyber attacks where attackers create fake or malicious websites to steal sensitive user information such as usernames, passwords, banking details, and personal data. These attacks exploit user trust and are difficult to detect because phishing domains are often newly created and short-lived.

This project presents a **Network-Based Phishing Detection Tool** that captures live network traffic, analyzes DNS queries and HTTP requests, and detects phishing attempts using a combination of **heuristic rules** and a **machine learning model**.

---

## ❗ Problem Statement

Phishing websites steal user credentials by impersonating legitimate websites. Traditional security systems often fail to detect newly created phishing domains in real time. Therefore, there is a need for an automated system that can analyze network traffic and dynamically identify phishing attempts.

---

## 🎯 Objectives

- Capture live DNS and HTTP network traffic  
- Extract domains and URLs from packets  
- Analyze suspicious URL and domain patterns  
- Detect phishing attempts using rule-based logic  
- Improve detection accuracy using machine learning  
- Generate real-time alerts and logs  

---

## ✨ Features

- DNS traffic inspection  
- HTTP GET and POST request inspection  
- Rule-based phishing detection  
- Machine Learning–based phishing detection  
- Real-time alerts on terminal  
- Logging of detected phishing attempts  
- Cross-platform support (Windows / Linux)  

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Libraries
- Scapy  
- Requests  
- Scikit-learn  
- Joblib  

### Operating System
- Windows / Linux

---

## 🏗️ System Architecture

Network Traffic
↓
Packet Capture (Scapy)
↓
DNS & HTTP Analysis
↓
Rule-Based Detection
↓
ML-Based Classification
↓
Alert Generation & Logging


---

## ⚙️ How the System Works

### 1. Packet Capture
The system captures live **DNS (UDP port 53)** and **HTTP (TCP port 80)** packets using the Scapy library.

### 2. DNS Traffic Inspection
- Extracts domain names from DNS queries  
- Checks for suspicious keywords, abnormal length, and IP-based domains  
- Applies a machine learning model to classify domains  

### 3. HTTP Traffic Inspection
- Inspects HTTP GET and POST requests  
- Extracts host and URL path  
- Detects phishing indicators in URLs  

### 4. Rule-Based Detection
The rule-based system flags URLs/domains based on:
- Suspicious keywords (login, verify, secure, bank, update)  
- Long or abnormal domain names  
- Numeric IP-based URLs  

### 5. Machine Learning Detection
A **Random Forest classifier** is trained on phishing and legitimate URLs. The trained model predicts whether a domain or URL is phishing or safe in real time.

### 6. Alert and Logging
When phishing activity is detected:
- Alerts are displayed on the terminal  
- Details are stored in a log file for future analysis  

---

## 🤖 Machine Learning Model Details

- Algorithm: Random Forest Classifier  
- Feature Type: URL lexical features  
- Labels:
  - `1` → Phishing  
  - `0` → Legitimate  
- Model is trained once and saved as `.pkl` files  
- Loaded dynamically during execution  

---

## 📂 Project Structure
```
MiniProjectCyber/
│
├── src/
│   ├── phishing_detector.py
│   ├── packet_sniffer.py
│   ├── url_analyzer.py
│   ├── http_analyzer.py
│   ├── ml_model.py
│   └── ml_detector.py
│
├── doc/
│   ├── synopsis.md
│   ├── problem_statement.md
│   └── methodology.md
│
├── logs/
│   └── detected_phishing.log
│
├── phishing_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## 🔧 Installation & Setup

### Step 1: Clone Repository
```bash
git clone https://github.com/shortsays/MiniProjectCyber
cd MiniProjectCyber
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run the Project

⚠️ **Run Terminal / PowerShell as Administrator**

### Step 1: Train the ML Model (One-Time)
```bash
python src/ml_model.py
```

### Step 2: Start Phishing Detection
```bash
python src/phishing_detector.py
```

---

## 🧪 Sample Output
```
Starting Network-Based Phishing Detection Tool...
Monitoring DNS and HTTP traffic...
[DNS ALERT] Phishing Domain: secure-login-update.com
[HTTP ALERT] Phishing URL: verify-bank-account.net/login
```

---

## 📜 Logs
All detected phishing activities are stored in:
```
logs/detected_phishing.log
```

**Example:**
```
2026-01-24 11:30:22 - DNS: secure-login-update.com
```

---

## ⚠️ Limitations
- May generate false positives
- Limited dataset for ML training
- HTTPS payload is not deeply inspected

---

## 🚀 Future Enhancements
- Deep learning–based phishing detection
- HTTPS traffic inspection
- Browser extension integration
- Web-based monitoring dashboard
- Whitelist and blacklist mechanisms

---

## 🏁 Conclusion
The Network-Based Phishing Detection Tool demonstrates an effective approach to detecting phishing attacks using real-time network traffic analysis. By combining rule-based techniques with machine learning, the system improves detection accuracy and provides a strong foundation for advanced cybersecurity applications.

---

## 👥 Team Details

**Team Leader**
- Ankit Saraswat

**Team Members**
- Nancy Paul
- Sujal Singh
- Riya Devi