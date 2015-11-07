import sys
import itertools

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers = [int(x) for x in line.split(',')]
        print(len([x for x in itertools.combinations(numbers, 4) if sum(x) == 0]))

lines.close()
