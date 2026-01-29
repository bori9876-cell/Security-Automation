failed_count = 0
threshold = 3

with open("sample.log", 'r') as log:
    for line in log:
        if "ERROR" in line:
            failed_count += 1
        else:
            failed_count += 0
        

if failed_count >= threshold:
    print("ALERT!: Possible brute force attack detected!")
else:
    print("No brute force activity detected.")