import sys

def parseCoords(x):
    return [int(y) for y in x.strip('[').strip(']').split(',')]

def size2(a, b):
    return sorted([abs(a[0] - b[0]), abs(a[1] - b[1])])

def size3(a, b):
    s = []
    s.append(sorted([abs(a[0] - b[0]), abs(a[1] - b[1])]))
    s.append(sorted([abs(a[0] - b[0]), abs(a[2] - b[2])]))
    s.append(sorted([abs(a[1] - b[1]), abs(a[2] - b[2])]))
    return s

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        hole, bricks = line.split('|')
        holecoords = [parseCoords(x) for x in hole.split(' ')]
        holesize = size2(holecoords[0], holecoords[1])
        
        bricks = [[y for y in x.strip('(').strip(')').split(' ')] for x in bricks.split(';')]
        bricks = [[int(x[0]), parseCoords(x[1]), parseCoords(x[2])] for x in bricks]
        passed = []
        for brick in bricks:
            s = size3(brick[1], brick[2])
            if s[0][0] <= holesize[0] and s[0][1] <= holesize[1]:
                passed.append(brick[0])
            elif s[1][0] <= holesize[0] and s[1][1] <= holesize[1]:
                passed.append(brick[0])
            elif s[2][0] <= holesize[0] and s[2][1] <= holesize[1]:
                passed.append(brick[0])
        print(','.join([str(x) for x in sorted(passed)]) if len(passed) > 0 else '-')

lines.close()
