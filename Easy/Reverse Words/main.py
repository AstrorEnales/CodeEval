import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        partsReverse = line.split(' ')[::-1]
        print(' '.join(partsReverse))

lines.close()
