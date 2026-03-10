#line = "ERROR: Failed to connect to database\n"
#keyword = "ERROR"

#print(repr(line))
#print(repr(line.replace(keyword, "")))
#print(repr(line.replace(keyword, "").strip()))
#print(repr(line.replace(keyword, "").strip().lstrip(": ")))

#scan = {
#    "ERROR": [(3,"Failed login"), (9,"Disk full")],
#    "WARNING": [(8,"CPU high")]
#}

#print(scan.items())
keywords = ["ERROR", "WARNING"]

lines = [
    "INFO: System starting",
    "ERROR: Failed login",
    "WARNING: CPU high",
    "ERROR: Disk full"
]

results = {}

line_number = 0

for line in lines:
    line_number += 1
    print("\nReading line:", line)

    for keyword in keywords:

        if keyword not in results:
            results[keyword] = []

        if keyword in line:
            clean_line = line.replace(keyword, "").strip()
            clean_line = clean_line.lstrip(": ")

            results[keyword].append((line_number, clean_line))

            print("Match found →", keyword)
            print("Dictionary now →", results)

print("\nFINAL DICTIONARY:")
print(results)