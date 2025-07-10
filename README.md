# LogParser360

A professional-grade Python tool for **analyzing Linux system logs**, generating structured reports, and **sending real-time email alerts** for critical events such as failed logins and system errors.

---

## 🔍 Overview

**LogParser360** automates the process of:

- Parsing large log files (`auth.log`, `syslog`, etc.)
- Detecting suspicious or critical events
- Generating JSON-based reports
- Sending email notifications when defined thresholds are exceeded

Designed for developers, system administrators, and security-conscious users.

---

## 🛠️ Features

- ✅ Parses Linux log files
- ✅ Detects:
  - Failed SSH login attempts
  - sudo command usage
  - error & warning messages
- ✅ Generates structured `JSON` reports
- ✅ Sends real-time **email alerts** using Gmail SMTP
- ✅ Threshold-based alert logic
- ✅ Lightweight & Python-only (no 3rd party libraries)
- ✅ Easy to extend and integrate into CI or cron jobs

---

## 🚀 How to Use

### 1. Clone the Repo

```bash
git clone https://github.com/Udi1988/logparser360.git
cd logparser360

### 2. Create a Python Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 3. 3. Configure Email Alerts
Edit parser.py and update these lines with your real email details:
SENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
RECIPIENT_EMAIL = "recipient@example.com"

### 4. Run the Parser
python3 parser.py

Your report will be saved to reports/report.json, and an email will be sent if issues are detected.

---

 Folder Structure
logparser360/
├── parser.py               # Main script
├── utils/
│   └── email_alert.py      # Email utility
├── sample_logs/
│   └── auth.log            # Test log file
├── reports/
│   └── report.json         # Output report
├── README.md
└── .gitignore

---

👤 Author
Udeshan Moodley
Software Tester | Automation Enthusiast




