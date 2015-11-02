import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = [int(x) for x in line.split(' ')]
        partsSet = sorted(list(set(parts)))
        counts = [len([y for y in parts if y == x]) for x in partsSet]
        unique = [x for x in range(len(counts)) if counts[x] == 1]
        print(str(parts.index(partsSet[unique[0]]) + 1) if len(unique) > 0 else '0')
        

lines.close()
