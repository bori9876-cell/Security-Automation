def count_keywords_in_file(filename, keywords_list):
    counts = {key.lower(): 0 for key in keywords_list}
    with open(filename, 'r') as f:
        for line in f:
            line_lower = line.lower()
            for key in counts:
                if key in line_lower:
                    counts[key] += 1
    return counts

result = count_keywords_in_file('sample.log', ['ERROR', 'WARNING'])
print(result)