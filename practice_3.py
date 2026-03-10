counts = {
    "error": 0,
    "warning": 0
}

with open("sample.log", "r") as log:
    for line in log:
        line_lower = line.lower()
        if "error" in line_lower: # if error shows up in the line at all, count it once
            counts["error"] += 1
        if "warning" in line_lower: # if warning shows up in the line at all, count it once
            counts["warning"] += 1
            
print(counts)