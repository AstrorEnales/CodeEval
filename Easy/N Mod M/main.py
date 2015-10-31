import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        n, m = [int(x) for x in line.split(',')]
        if m > n:
            print(n)
        else:
            intPart = n / m
            floatPart = n / float(m)
            diff = floatPart - intPart
            print(int(round(diff * m)))
        

lines.close()
