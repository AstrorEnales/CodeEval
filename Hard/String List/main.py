import sys
import itertools

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        n, s = line.split(',')
        n = int(n)
        alphabet = sorted(list(set(s)) * n)
        elements = sorted(set(list(itertools.permutations(alphabet, n))))
        print(','.join([''.join(x) for x in elements]))

lines.close()
