import sys

def parseCoord(x):
    return [int(y) for y in x[1:len(x) - 1].split(',')]

def distSquared(a, b):
    return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2

def perpendicular(a, b, c, d):
    dista = set([distSquared(a, x) for x in [b, c, d]])
    distb = set([distSquared(b, x) for x in [a, c, d]])
    distc = set([distSquared(c, x) for x in [b, a, d]])
    distd = set([distSquared(d, x) for x in [b, c, a]])
    return len(dista) == 2 and len(distb) == 2 and len(distc) == 2 and len(distd) == 2

def isSquare(a, b, c, d):
    center = [sum([x[0] for x in coords]) / 4.0, sum([x[1] for x in coords]) / 4.0]
    dista = distSquared(center, a)
    distb = distSquared(center, b)
    distc = distSquared(center, c)
    distd = distSquared(center, d)
    if (dista == distb and dista == distc and dista == distd) == False:
        return False
    return perpendicular(a, b, c, d)

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        coords = [parseCoord(x) for x in line.split(', ')]
        print('true' if len(coords) == 4 and isSquare(*coords) else 'false')

lines.close()
