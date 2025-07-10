import re
import json
from datetime import datetime

def parse_log(file_path):
    failed_logins = 0
    sudo_attempts = 0
    errors = 0
    warnings = 0
    top_errors = {}

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            if "Failed password" in line:
                failed_logins += 1
            if "sudo" in line:
                sudo_attempts += 1
            if "error" in line.lower():
                errors += 1
                err_msg = line.strip()
                top_errors[err_msg] = top_errors.get(err_msg, 0) + 1
            if "warn" in line.lower():
                warnings += 1

    summary = {
        "total_lines": sum(1 for _ in open(file_path)),
        "failed_logins": failed_logins,
        "sudo_attempts": sudo_attempts,
        "errors": errors,
        "warnings": warnings,
        "top_errors": sorted(top_errors, key=top_errors.get, reverse=True)[:3],
        "last_updated": datetime.now().isoformat()
    }

    return summary

def save_report(data, path='reports/report.json'):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def main():
    import os
    os.makedirs('reports', exist_ok=True)
    report = parse_log('sample_logs/auth.log')
    save_report(report)
    print("✔ Log analysis complete. Report saved to reports/report.json")

if __name__ == '__main__':
    main()
