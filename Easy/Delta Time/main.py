import sys
import time
import datetime

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        a, b = sorted([datetime.datetime.strptime(x, "%H:%M:%S") for x in line.split(' ')])
        hours, remainder = divmod((b - a).seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print('%02d:%02d:%02d' % (hours, minutes, seconds))

lines.close()
