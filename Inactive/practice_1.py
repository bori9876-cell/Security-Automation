count = 0

with open("sample.log", "r") as log:
    for line in log:
        if "ERROR" in line:
            count += 1
            
print(count)