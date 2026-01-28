from datetime import datetime
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python log_alert.py <log_filename>")
        return

    log_filename = sys.argv[1]

    suspicious_keywords = ["ERROR", "WARNING", "DENIED", "FAILED"]
    counts = {}

    with open(log_filename, "r") as file:
        for line in file:
            line_lower = line.lower()
            matched_keywords = set()

            for keyword in suspicious_keywords:
                if keyword.lower() in line_lower:
                    matched_keywords.add(keyword)

            for keyword in matched_keywords:
                counts[keyword] = counts.get(keyword, 0) + 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("report.txt", "a") as report_file:
        report_file.write(f"=== Report: {timestamp} ===\n")
        for keyword, count in counts.items():
            report_file.write(f"{keyword}: {count}\n")
        report_file.write("\n")

    print(f"Report saved to report.txt (from {log_filename})")


if __name__ == "__main__":
    main()
