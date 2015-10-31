import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        zeroCount, limit = [int(x) for x in line.split(' ')]
        numbers = ['{0:b}'.format(x) for x in range(limit + 1)[1::]]
        print(len([x for x in numbers if len([y for y in x if y == '0']) == zeroCount]))

lines.close()
 
