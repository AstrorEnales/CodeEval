import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        num, p1, p2 = [int(x) for x in line.split(',')]
        numBin = '{0:b}'.format(num)
        print('true' if numBin[len(numBin) - p1] == numBin[len(numBin) - p2] else 'false')

lines.close()
 
