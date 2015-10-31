import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split(' ')
        print(' '.join([x[0].upper() + x[1::] for x in parts]))

lines.close()
