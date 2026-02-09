def scan_file(filename, keywords):
    with open(filename, 'r') as f:
        for line in f:
            line_lower = line.lower()
            
            for key in keywords:
                if key.lower() in line_lower:
                    print('Found:', key, '->', line.strip())

run = scan_file('sample.log', ['ERROR', "WARNING"])
print(run)