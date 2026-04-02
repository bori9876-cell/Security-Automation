def count_keywords_in_file(filename, keywords_list):
    with open(filename, 'r') as f:
        results = []
        for line in f:
            line_lower = line.lower()
            line_keywords = []
            for key in keywords_list:
                if key.lower() in line_lower:
                    line_keywords.append(key)
            if line_keywords:
                results.append(line_keywords)
    return results

result = count_keywords_in_file('sample.log', ['ERROR', 'WARNING'])
print(result)