counts = {
    "error": 0,
    "warning": 0
}

with open("sample.log", "r") as log:
    for line in log:
        line_lower = line.lower()
        if "error" in line_lower:
            counts["error"] += 1
        if "warning" in line_lower:
            counts["warning"] += 1
            
print(counts)