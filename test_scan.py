scan = {
    "ERROR": [
        (3, "Failed login"),
        (5, "Timeout"),
        (9, "Disk full")
    ],
    "WARNING": [(8, "CPU high")]
}

print(scan)

most_common = None
highest_count = 0

for key, matches in scan.items():
    count = len(matches)
    print(key, count)
    
    if count > highest_count:
        highest_count = count
        most_common = key

print("Most common:", most_common, "with", highest_count)