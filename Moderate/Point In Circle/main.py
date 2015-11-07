import sys
import math

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        line = line.replace('Center: ', '').replace(' Radius: ', '').replace(' Point: ', '').replace('(', '').replace(')', '')
        center, radius, point = line.split(';')
        center = [float(x) for x in center.split(', ')]
        radius = abs(float(radius))
        point = [float(x) for x in point.split(', ')]
        distx = center[0] - point[0]
        disty = center[1] - point[1]
        dist = math.sqrt(distx * distx + disty * disty)
        print('true' if dist <= radius else 'false')

lines.close()
