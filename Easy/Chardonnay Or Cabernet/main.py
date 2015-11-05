import sys
from collections import Counter

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split(' | ')
        names = parts[0].split(' ')
        countsInPattern = Counter(parts[1])
        matching = []
        for name in names:
            countsInName = Counter(name)
            if all([x in countsInName and countsInName[x] >= countsInPattern[x] for x in countsInPattern]):
                matching.append(name)
        print(' '.join(matching) if len(matching) > 0 else 'False')

lines.close()
