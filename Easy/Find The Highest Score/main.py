import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = [[int(y) for y in x.split(' ')] for x in line.split(' | ')]
        print(' '.join([str(max([parts[j][i] for j in range(len(parts))])) for i in range(len(parts[0]))]))

lines.close()
