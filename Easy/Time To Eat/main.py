import sys
import time
import datetime

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        times = sorted([time.strptime(x, "%H:%M:%S") for x in line.split(' ')])[::-1]
        print(' '.join(['%02d:%02d:%02d' % (x.tm_hour, x.tm_min, x.tm_sec) for x in times]))

lines.close()
