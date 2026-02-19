RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"
# =========================
# A) LOAD KEYWORDS FROM A FILE
# -------------------------
# 1. Create a function called load_keywords(filename)
# 2. Open the file in read mode
# 3. Loop through each line in the file
# 4. Strip whitespace/newlines from each line
# 5. Store keywords in a list
# 6. Return the list
def load_keywords(filename):
    keywords = []
    with open(filename, 'r') as f:
        for line in f:
            keywords.append(line.strip())
    return keywords

# =========================
# B) SCAN THE LOG FILE
# -------------------------
# 1. Create a function called scanner(filename, keywords)
# 2. Open the log file in read mode
# 3. Loop through each line and keep track of line numbers
# 4. For each keyword, check if it exists in the line
# 5. Remove the keyword from the line to clean the message
# 6. Store matches in a dictionary like:
#    results["ERROR"] = [(line_number, cleaned_text), ...]
# 7. Return the results dictionary
def scanner(filename, keywords):
    results = {}
    line_number = 0
    with open(filename, 'r') as f:        
        for line in f:
            line_number += 1         
            for keyword in keywords:
                if keyword not in results:
                    results[keyword] = []
                if keyword in line:
                    clean_line = line.replace(keyword, "").strip()
                    clean_line = clean_line.lstrip(": ")
                    results[keyword].append((line_number, clean_line))
    return results

# =========================
# C) PRINT RESULTS WITH COLORS
# -------------------------
# 1. Define color codes for ERROR, WARNING, INFO
# 2. Loop through the results dictionary
# 3. Choose a color depending on the keyword
# 4. Print keyword, line number, and cleaned text
keywords = load_keywords("keywords.txt")
scan = scanner("sample.log", keywords)

for key, matches in scan.items():
    for ln, text in matches:
        if key == "ERROR":
            color = RED
        elif key == "WARNING":
            color = YELLOW
        elif key == "INFO":
            color = GREEN
        else:
            color = RESET
        print(color + key + RESET, "on line", ln, ":", text)