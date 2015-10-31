import sys
import re
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        text, find = line.split(',')
        indices = [m.start() for m in re.finditer('(?=' + find + ')', text)]
        if len(indices) > 0:
            print(indices[len(indices) - 1])
        else:
            print('-1')

lines.close()
