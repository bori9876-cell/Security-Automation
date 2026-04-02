RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

scores = {
    "ERROR": 3,
    "WARNING": 2,
    "INFO": 1
}

total_score = 0

def load_keywords(filename):
    keywords = []
    with open(filename, 'r') as f:
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
                    for k in keywords:
                        clean_line = clean_line.replace(k, "")
                    clean_line = clean_line.lstrip(": ")
                    results[keyword].append((line_number, clean_line))
    return results

keywords = load_keywords("keywords.txt")
scan = scanner("sample.log", keywords)

colors = {
    "ERROR" : RED,
    "WARNING" : YELLOW,
    "INFO" : GREEN
}

most_common = None
highest_count = 0

for key, matches in scan.items():
    count = len(matches)
    if count > highest_count:
        highest_count = count
        most_common = key
    print(key, count)

    color = colors.get(key, RESET)
    
    for ln, text in matches:
        print(color + key + RESET, "on line", ln, ":", text)

print("Most common:", most_common, "with", highest_count)