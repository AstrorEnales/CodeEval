import sys
import re
from collections import Counter

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        chars = [line[match.start()].lower() for match in re.finditer('[a-zA-Z]', line)]
        counts = Counter(chars)
        sortedCounts = sorted(counts.values())[::-1]
        value = 26
        result = 0
        for x in sortedCounts:
            result = result + (x * value)
            value = value - 1
        print(result)

lines.close()
