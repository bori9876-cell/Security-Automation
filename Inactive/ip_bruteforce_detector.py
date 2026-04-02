from datetime import datetime

threshold = 3
time_window = 60

# store failed attempts per IP
failed_attempts = {}

with open("sample.log", "r") as log:
    for line in log:
        if "ERROR" in line and line[0].isdigit():
            timestamp_str = line[:19]
            event_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H %M %S")

            ip_start = line.find("ip=")
            ip_end = line.find(" ", ip_start)
            ip_address = line[ip_start + 3:ip_end]