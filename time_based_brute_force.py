from datetime import datetime

threshold = 3
time_window = 60  # seconds
failed_times = []

with open("sample.log", "r") as log:
    for line in log:
        if "ERROR" in line and line[0].isdigit():
            timestamp_str = line[:19]  # first 19 chars = timestamp
            event_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            failed_times.append(event_time)

for i in range(len(failed_times) - threshold + 1):
    window = failed_times[i:i + threshold]
    delta = (window[-1] - window[0]).total_seconds()
    if delta <= time_window:
        print("⚠️ ALERT: Brute force attack detected within 60 seconds!")
        break
else:
    print("No brute force activity detected.")
