import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        o, p, q, r = [int(x) for x in line.split(' ')]
        if o == q and p == r:
            print('here')
        else:
            direction = ''
            if r - p > 0:
                direction = direction + 'N'
            elif r - p < 0:
                direction = direction + 'S'
            if q - o > 0:
                direction = direction + 'E'
            elif q - o < 0:
                direction = direction + 'W'
            print(direction)

lines.close()
