import sys
import re

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split(' ')
        pattern = '^' + parts[0].replace('.', '\.').replace('?', '.').replace('*', '.*') + '$'
        matches = [re.findall(pattern, x) for x in parts[1:]]
        result = ' '.join([str(x[0]) for x in matches if len(x) > 0])
        print(result if len(result) > 0 else '-')

lines.close()
