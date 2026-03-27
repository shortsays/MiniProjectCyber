# 📊 System Architecture

## 1. Overview
The system is designed as a modular pipeline where network data flows through multiple processing layers for analysis and detection.

---

## 2. Architecture Components

### a. Packet Sniffer
Captures real-time network traffic using Scapy. It listens to DNS, HTTP, and HTTPS packets.

### b. Protocol Analyzer
Extracts relevant data:
- DNS → domain names
- HTTP → full URLs
- HTTPS → domain names via TLS SNI

### c. Feature Extraction Module
Converts URLs/domains into numerical features such as:
- Length
- Special characters
- Presence of IP
- Keywords

### d. Detection Engine
Combines:
- Rule-based detection
- Machine learning model

### e. Database
Stores detected phishing logs in SQLite for persistence.

### f. Dashboard
A Flask-based web interface that visualizes logs and analytics in real time.

---

## 3. Workflow

1. Capture network packet  
2. Extract URL/domain  
3. Generate features  
4. Apply ML + rules  
5. Detect phishing  
6. Store in database  
7. Display on dashboard  

---

## 4. Summary
The architecture ensures real-time detection, modular design, and scalability for future improvements.