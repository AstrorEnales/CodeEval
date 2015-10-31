import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        matrixLines = line.split(',')
        rightXIndices = [x.rindex('X') for x in matrixLines]
        leftYIndices = [x.index('Y') for x in matrixLines]
        steps = [leftYIndices[i] - rightXIndices[i] - 1 for i in range(len(rightXIndices))]
        print(min(steps))

lines.close()
