# 🛡️ Network-Based Phishing Detection Tool

A real-time **network-based phishing detection system** that analyzes **DNS, HTTP, and HTTPS traffic** to identify phishing attempts using **rule-based techniques and machine learning**.

---

## 📌 Introduction

Phishing is one of the most common cyber attacks where attackers create fake or malicious websites to steal sensitive user information such as usernames, passwords, banking details, and personal data. These attacks exploit user trust and are difficult to detect because phishing domains are often newly created and short-lived.

This project presents a **Network-Based Phishing Detection Tool** that captures live network traffic, analyzes DNS queries, HTTP requests, and HTTPS domains, and detects phishing attempts using a combination of **heuristic rules** and a **machine learning model**.

---

## ❗ Problem Statement

Phishing websites steal user credentials by impersonating legitimate websites. Traditional security systems often fail to detect newly created phishing domains in real time. Therefore, there is a need for an automated system that can analyze network traffic and dynamically identify phishing attempts.

---

## 🎯 Objectives

- Capture live DNS, HTTP, and HTTPS network traffic  
- Extract domains and URLs from packets  
- Analyze suspicious URL and domain patterns  
- Detect phishing attempts using rule-based logic  
- Improve detection accuracy using machine learning  
- Generate real-time alerts and logs  
- Visualize phishing activity using a live dashboard  

---

## ✨ Features

- DNS traffic inspection  
- HTTP request inspection  
- HTTPS detection using TLS SNI 🔥  
- Rule-based phishing detection  
- Machine Learning–based phishing detection  
- Hybrid detection (ML + Rules)  
- Real-time alerts on terminal  
- SQLite database logging  
- Live Flask dashboard with graphs 📊  
- Noise filtering and duplicate removal  

---

## 🛠️ Technologies Used

### Programming Language
- Python  

### Libraries
- Scapy  
- Flask  
- SQLite3  
- Scikit-learn  
- Joblib  
- Chart.js  

### Operating System
- Windows / Linux  

---

## 🏗️ System Architecture

Network Traffic  
↓  
Packet Capture (Scapy)  
↓  
DNS / HTTP / HTTPS Analysis  
↓  
Feature Extraction  
↓  
Rule-Based Detection  
↓  
ML-Based Classification  
↓  
Alert Generation & Logging  
↓  
Dashboard Visualization  

---

## ⚙️ How the System Works

### 1. Packet Capture
The system captures live:
- DNS (UDP port 53)  
- HTTP (TCP port 80)  
- HTTPS (TLS handshake)  

---

### 2. DNS Traffic Inspection
- Extracts domain names from DNS queries  
- Checks for suspicious keywords and patterns  
- Applies machine learning model  

---

### 3. HTTP Traffic Inspection
- Extracts host and path  
- Forms complete URL  
- Detects phishing indicators  

---

### 4. HTTPS Detection (TLS SNI)
- Extracts domain names from encrypted traffic  
- Enables phishing detection even for HTTPS websites  

---

### 5. Rule-Based Detection
Flags URLs based on:
- Suspicious keywords (login, verify, bank, secure)  
- Long or abnormal domains  
- IP-based URLs  

---

### 6. Machine Learning Detection
- Model: **Random Forest Classifier**  
- Input: URL features  
- Output:
  - `1` → Phishing  
  - `0` → Legitimate  
- Provides confidence score  

---

### 7. Hybrid Detection
Combines:
- Rule-based detection  
- ML prediction  

Improves accuracy and reduces false positives.

---

### 8. Alert and Logging
When phishing is detected:
- Alert shown in terminal  
- Stored in:
  - Log file  
  - SQLite database  

---

### 9. Dashboard Visualization
- Built using Flask  
- Displays:
  - Live phishing logs  
  - Confidence scores  
  - Graph analytics  
- Auto-refresh every few seconds  

---

## 🤖 Machine Learning Model Details

- Algorithm: Random Forest Classifier  
- Feature Type: URL lexical features  
- Labels:
  - `1` → Phishing  
  - `0` → Legitimate  
- Model saved as `.pkl` file  
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
│   ├── ml_detector.py
│   ├── feature_extractor.py
│   └── database.py
│
├── templates/
│   └── dashboard.html
│
├── doc/
│   ├── problem_statement.md
│   └── methodology.md
│
├── logs/
│   └── detected_phishing.log
│
├── models/
│   └── phishing_model.pkl
│
├── app.py
├── dataset.csv
├── phishing.db
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
cd src
python model_training.py
```

### Step 2: Start Phishing Detection
```bash
python src/phishing_detector.py
```

### Step 3: Run Dashboard
```bash
python app.py
```

### Step 4: Open Dashboard
```bash
http://127.0.0.1:5000
```

---

## 🧪 Sample Output
```
🛡️ Phishing Detection Started...
[CHECK] login-paypal-secure.com → 0.92

🚨 PHISHING ALERT 🚨
URL       : login-paypal-secure.com
Source    : DNS
Confidence: 0.92
```

---

## 📜 Logs
All detected phishing activities are stored in:
```
logs/detected_phishing.log
```

**Example:**
```
[11:25:10] DNS | login-paypal-secure.com | 0.91
```

---

## ⚠️ Limitations
- Possible false positives
- Limited dataset for ML
- HTTPS payload not fully decrypted

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