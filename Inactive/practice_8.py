def logscan(filename, keywords):
    counts = {}

    with open(filename, 'r') as f:
        for line in f:
            line_lower = line.lower()
            for keyword in keywords:
                keyword_lower = keyword.lower()
                if keyword_lower not in counts:
                    counts[keyword_lower] = 0
                if keyword_lower in line_lower:
                    counts[keyword_lower] += 1
                
    return counts

logscanrun = logscan('sample.log', ['ERROR', 'INFO', 'WARNING'])
print(logscanrun)