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
