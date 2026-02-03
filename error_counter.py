import sys

default_message = "Enter at least 3 arguments"

if len(sys.argv) < 3:
    print(default_message)
    sys.exit()

def count_keywords_in_file(filename, keywords_list):
    counts = {key.lower(): 0 for key in keywords_list}
    with open(filename, 'r') as f:
        for line in f:
            line_lower = line.lower()
            for key in counts:
                if key in line_lower:
                    counts[key] += 1
    return counts

result = count_keywords_in_file(sys.argv[1], sys.argv[2:])

for key, value in result.items():
    print(f"{key}: {value}")
