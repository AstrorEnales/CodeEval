import sys
from collections import OrderedDict

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        seq = line.split(',')
        print(','.join(list(OrderedDict.fromkeys(seq))))

lines.close()
