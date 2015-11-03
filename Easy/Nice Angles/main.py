import sys
import math

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        num = float(line)
        value1 = int(num)
        num = (num - value1) * 60.0
        value2 = int(num)
        num = (num - value2) * 60.0
        value3 = int(num)
        print("%d.%02d'%02d\"" % (value1, value2, value3))
        

lines.close()
