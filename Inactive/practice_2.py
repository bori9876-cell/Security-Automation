count = 0

with open("sample.log", "r") as log:
    for line in log:
        line_lower = line.lower()
        if "error" in line_lower:
            count += 1
            
print(count)