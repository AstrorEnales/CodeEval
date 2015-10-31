import sys

letters = 'abcdefgh'

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        a, b = [[int(y) for y in x.split(' ')] for x in line.split(' | ')]
        print(' '.join([str(a[i] * b[i]) for i in range(len(a))]))

lines.close()
