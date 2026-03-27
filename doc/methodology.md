# 📌 Methodology

## 1. Overview
The proposed system follows a hybrid approach combining rule-based detection and machine learning techniques to identify phishing attempts in real-time network traffic. The system continuously monitors DNS, HTTP, and HTTPS traffic and analyzes extracted data to detect suspicious activities.

---

## 2. Network Traffic Capture
The system uses the Python library Scapy to capture live network packets. It listens to:
- DNS traffic (port 53)
- HTTP traffic (port 80)
- HTTPS traffic (TLS handshake)

This allows the system to monitor user activity in real time.

---

## 3. Data Extraction

### a. DNS Analysis
The system extracts domain names from DNS queries. These domains are analyzed to detect suspicious patterns.

### b. HTTP Analysis
For HTTP traffic, the system extracts:
- Host
- Path

These are combined to form a complete URL.

### c. HTTPS Analysis (TLS SNI)
For HTTPS traffic, the system extracts the Server Name Indication (SNI) from TLS packets, which reveals the domain name even in encrypted communication.

---

## 4. Feature Engineering
Each URL/domain is converted into numerical features for machine learning. The features include:
- URL length
- Number of dots (.)
- Number of hyphens (-)
- Presence of HTTPS
- Presence of IP address
- Number of digits
- Number of special characters

These features help distinguish between legitimate and phishing URLs.

---

## 5. Machine Learning Model
A Random Forest Classifier is used for phishing detection. The model is trained on a dataset of labeled URLs where:
- 0 represents legitimate websites
- 1 represents phishing websites

The model outputs:
- Prediction (phishing or safe)
- Confidence score

---

## 6. Rule-Based Detection
In addition to ML, the system uses rule-based checks such as:
- Presence of suspicious keywords (e.g., login, verify, bank)
- Unusual URL length
- IP address in URL

This helps detect phishing attempts that may not be captured by the ML model.

---

## 7. Hybrid Detection Mechanism
The system combines both approaches:
- Rule-based detection
- Machine learning prediction

A URL is flagged as phishing if:
- It is suspicious and has moderate ML confidence, OR
- It has high ML confidence

This reduces false positives and improves detection accuracy.

---

## 8. Logging and Storage
Detected phishing attempts are:
- Logged into a text file
- Stored in a SQLite database

Each log contains:
- Timestamp
- Source (DNS/HTTP/HTTPS)
- URL/domain
- Confidence score

---

## 9. Dashboard Visualization
A Flask-based web dashboard is used to display:
- Real-time phishing logs
- Confidence scores
- Graphical analytics using Chart.js

The dashboard updates automatically to show live network activity.

---

## 10. Noise Filtering and Optimization
To improve performance:
- Duplicate URLs are filtered
- Trusted domains (e.g., Microsoft, GitHub) are ignored
- Clean formatting is applied to logs

---

## 11. Summary
The system provides a real-time, scalable, and efficient phishing detection solution by combining:
- Network packet analysis
- Feature-based machine learning
- Rule-based heuristics
- Live visualization dashboard

This approach ensures accurate detection while maintaining system performance.