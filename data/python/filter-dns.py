import datetime
with open('.././rules.txt', 'r') as input_file, open('.././dns.txt', 'w') as output_file:
    for line in input_file:
        line = line.strip()        
        if len(line) >= 2 and line.startswith("||") and line.endswith("^"):
            output_file.write(line + '\n')
