RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

def load_keywords(filename):
    keywords = []
    with open(filename, "r") as f:
        for line in f:
            keywords.append(line.strip())
    return keywords

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

keywords = load_keywords("keywords.txt")
scan = scanner('sample.log', keywords)

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
        print(color + key + RESET, "on line", ln, ':', text)
