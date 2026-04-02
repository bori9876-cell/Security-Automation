def scan_file(filename, keywords):
    results = []
    with open(filename, 'r') as f:
        for line in f:
            line_lower = line.lower()
            
            for key in keywords:
                if key.lower() in line_lower:
                    results.append((key, line.strip()))

    return results

run = scan_file('sample.log', ['ERROR', "WARNING"])
print(run)