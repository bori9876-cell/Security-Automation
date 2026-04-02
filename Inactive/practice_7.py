def counter(filename, keywords):

    severity = {
        "error": 3,
        "warning": 2,
        "info": 1
    }

    total_score = 0
    counts = {}
    matches = []
    
    with open(filename, 'r') as f:
        for line in f:
            line_lower = line.lower()
            for keyword in keywords:
                keyword_lower = keyword.lower()
                if keyword_lower in line_lower:
                    if keyword not in counts:
                        counts[keyword_lower] = 0
                    counts[keyword_lower] += 1
                    matches.append(line.strip())
                    total_score = total_score + severity[keyword_lower]
    
    return counts, matches, total_score

counts, matches, total_score = counter('sample.log', ['ERROR', 'WARNING'])

print(counts)
print(total_score)