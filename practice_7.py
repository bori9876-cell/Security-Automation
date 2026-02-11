def counter(filename, keywords):
    counts = {}
    matches = []
    with open(filename, 'r') as f:
        for line in f:
            line_lower = line.lower()
            for keyword in keywords:
                keyword_lower = keyword.lower()
                if keyword_lower in line_lower:
                    if keyword not in counts:
                        counts[keyword] = 0
                    counts[keyword] += 1
                    matches.append(line.strip())
    
    return counts, matches

counts, matches = counter('sample.log', ['ERROR', 'WARNING'])

print(counts)
print(matches)