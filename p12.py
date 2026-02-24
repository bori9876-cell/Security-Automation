# =========================
# A) COLOR CODES (for terminal output)
# =========================

# Define RED, YELLOW, GREEN, RESET using ANSI escape codes
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

# =========================
# B) LOAD KEYWORDS FROM FILE
# =========================

# Make a function called load_keywords(filename)
# Inside it:
#   - create an empty list called keywords
#   - open the file
#   - loop through each line
#   - strip whitespace
#   - add the keyword to the list
#   - return the list
def load_keywords(filename):
    keywords = []
    with open(filename, 'r') as f:
        for line in f:
            keywords.append(line.strip())
    return keywords


# =========================
# C) SCANNER FUNCTION
# =========================

# Make a function called scanner(filename, keywords)
# Inside it:
#   - create a dictionary called results
#   - create a line_number counter starting at 0
#   - open the log file
#   - loop through each line
#       - increase line_number
#       - loop through each keyword
#           - if keyword not in results, make it an empty list
#           - if keyword is in the line:
#               - clean the line (remove keyword, strip whitespace, remove ": ")
#               - append (line_number, clean_line) as a tuple to results[keyword]
#   - return results
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
# D) LOAD KEYWORDS + RUN SCANNER
# =========================

# Call load_keywords("keywords.txt")
# Call scanner("sample.log", keywords)
# Store result in a variable
keywords = load_keywords("keywords.txt")
scan = scanner("sample.log", keywords)


# =========================
# E) PRINT RESULTS WITH COLORS
# =========================

# Loop through each keyword and its matches
# For each match:
#   - choose color based on keyword (ERROR red, WARNING yellow, INFO green)
#   - print keyword, line number, and text nicely
for key, matches in scan.items():
    for ln, text in matches:
        if key == "ERROR":
            color = RED
        elif key == "WARNING":
            color = YELLOW
        elif key == "INFO":
            color = GREEN
        else:
            color = "RESET"
        print(color + key + RESET, "on line", ln, ":", text)
    