def scanner(filename, keywords):
    counts = {}
    line_number = 0
    with open(filename, 'r') as f:
        for line in f:
            line_number += 1
            for keyword in keywords:
                if keyword not in counts:
                    counts[keyword] = 0
                if keyword in line:
                    counts[keyword] += 1
    return counts, line_number # not sure about this

scan = scanner('sample.log', ['ERROR', 'WARNING', 'INFO', 'DENIED'])
print(scan)