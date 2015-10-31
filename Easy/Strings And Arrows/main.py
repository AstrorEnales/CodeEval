import sys
import re
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        print(len([m.start() for m in re.finditer('(?=<--<<|>>-->)', line)]))

lines.close()
