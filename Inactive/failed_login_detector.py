import sys
from datetime import datetime
import re

default_log = "sample.log"
logfile = sys.argv[1] if len(sys.argv) > 1 else default_log

total_failed = 0
user_counts = {}

with open(logfile, "r") as f:
    for line in f:
        line_lower = line.lower()

        # if line indicates a failed login
        if ("failed" in line_lower and "login" in line_lower) or "access denied" in line_lower or "multiple failed attempts" in line_lower:
            total_failed += 1

            # extract username if present
            match = re.search(r"user\s+(\w+)", line, re.IGNORECASE)
            if match:
                user = match.group(1)
                user_counts[user] = user_counts.get(user, 0) + 1

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("report.txt", "a") as report:
    report.write(f"\n--- Failed Login Report {timestamp} ---\n")
    report.write(f"Total failed login attempts: {total_failed}\n")

    if user_counts:
        report.write("Failed logins by user:\n")
        for user, count in user_counts.items():
            report.write(f"{user}: {count}\n")

print("Failed login analysis complete.")
