import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = [float(x) for x in line.split(' ')]
        parts.sort()
        print(' '.join([("%.3f" % x) for x in parts]))

lines.close()
