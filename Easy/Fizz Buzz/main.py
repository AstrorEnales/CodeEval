import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    parts = line.split(' ')
    x = int(parts[0])
    y = int(parts[1])
    n = int(parts[2])
    out = ''
    for i in range(n + 1)[1::]:
        xDiv = (i % x) == 0
        yDiv = (i % y) == 0
        if xDiv and yDiv:
            out = out + ' FB'
        elif xDiv:
            out = out + ' F'
        elif yDiv:
            out = out + ' B'
        else:
            out = out + ' ' + str(i)
    print(out[1::])

lines.close()
