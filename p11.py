severity = {
    "ERROR": 3,
    "WARNING": 2,
    "INFO": 1
}

# Colors
RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

# A) Load keywords from a file into a list
def load_keywords(filename):
    keywords = []
    with open(filename, "r") as f:
        for line in f:
            # remove whitespace and newline
            keywords.append(line.strip())
    return keywords


# B) Scan the log file and collect matches
def scanner(filename, keywords):
    results = {}
    line_number = 0
    total_score = 0

    with open(filename, "r") as f:
        for line in f:
            line_number += 1

            for keyword in keywords:

                # make sure the keyword exists in the dictionary
                if keyword not in results:
                    results[keyword] = []

                # check if keyword is in the line
                if keyword in line:
                    clean_line = line.replace(keyword, "").strip()
                    clean_line = clean_line.lstrip(": ")

                    if keyword in severity:
                        total_score += severity[keyword]                    

                    # store line number + cleaned text
                    results[keyword].append((line_number, clean_line))

    return results, total_score


# Load keywords and scan
keywords = load_keywords("keywords.txt")
scan, score = scanner("sample.log", keywords)


# C) Print results with colors
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

print("\nTotal Risk Score:", score)