RED = "\033[31m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RESET = "\033[0m"

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
                    clean_line = clean_line.lstrip(": ")
                    results[keyword].append((line_number, clean_line))
    return results

def main():
    log_file = input("Enter log file name: ")
    keyword_file = input("Enter keywords file name: ")

    keywords = load_keywords(keyword_file)
    scan = scanner(log_file, keywords)
    colors = {
    "ERROR" : RED,
    "WARNING" : YELLOW,
    "INFO" : GREEN
    }
    
    for key, matches in scan.items():
        color = colors.get(key, RESET)
        for ln, text in matches:
            print(color + key + RESET, "on line", ln, ":", text)
        
if __name__ == "__main__":
    main()

    