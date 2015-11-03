import sys
import re

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        checks = [int(line[i]) == len([x for x in line if int(x) == i]) for i in range(len(line))]
        print(1 if all(checks) else 0)

lines.close()
