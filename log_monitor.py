from datetime import datetime

THRESHOLD = 2
ALERT_FILE = "alerted.txt"


error_count = 0
warning_count = 0
denied_count = 0
important_count = 0

try:
    with open("alert_file.txt", "r") as f:
        alerted = f.read().strip() == "1"
except FileNotFoundError:
    alerted = False

with open("sample.log", "r") as log:
    with open("important.log", "a") as out:
        for line in log:
            if "ERROR" in line:
                error_count += 1
                important_count += 1
                out.write(f"[{datetime.now()}] {line}")
            elif "WARNING" in line:
                warning_count += 1
                important_count += 1
                out.write(f"[{datetime.now()}] {line}")
            elif "DENIED" in line:
                denied_count += 1
                important_count += 1
                out.write(f"[{datetime.now()}] {line}")

print("Error:", error_count)
print("Warning:", warning_count)
print("Denied:", denied_count)
print("Total important:", important_count)

if important_count > THRESHOLD and not alerted:
    print("ALERT: High number of security events detected!")
    alerted = True
    with open(ALERT_FILE, "w") as f:
        f.write("1")