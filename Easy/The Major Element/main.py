import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = [int(x) for x in line.split(',')]
        partsSet = sorted(list(set(parts)))
        counts = [len([y for y in parts if y == x]) for x in partsSet]
        major = [x for x in range(len(counts)) if counts[x] > len(parts) / 2]
        print(str(partsSet[major[0]]) if len(major) > 0 else 'None')
        

lines.close()
