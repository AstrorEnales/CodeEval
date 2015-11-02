import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        x, n = [int(x) for x in line.split(',')]
        i = 1
        while n * i < x:
            i = i + 1
        print(n * i)

lines.close()
