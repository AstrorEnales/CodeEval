import sys
import math
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        a, b = line.split(') (')
        x1, y1 = a[1::].split(', ')
        x2, y2 = b[0:len(b) - 1].split(', ')
        xDist = int(x2) - float(x1)
        yDist = int(y2) - float(y1)
        print(int(math.sqrt(xDist * xDist + yDist * yDist)))

lines.close()
 
