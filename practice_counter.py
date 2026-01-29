import sys

def count_keywords_in_file(filename, keywords_list):
    # initialize counts
    counts = {key.lower(): 0 for key in keywords_list}

    # open and convert file to lower case, search keywords and add to counts by key
    with open(filename, "r") as f:
        for line in f:
            line_lower = line.lower()
            for key in counts:
                if key in line_lower:
                    counts[key] += 1

    return counts


filename = sys.argv[1] # first argument: the log file
keywords = sys.argv[2:] # all remaining arguments: the keywords

result = count_keywords_in_file(filename, keywords)

print(result)