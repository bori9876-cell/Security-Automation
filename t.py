line = "ERROR: Failed to connect to database\n"
keyword = "ERROR"

print(repr(line))
print(repr(line.replace(keyword, "")))
print(repr(line.replace(keyword, "").strip()))
print(repr(line.replace(keyword, "").strip().lstrip(": ")))