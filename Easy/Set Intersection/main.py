import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        a, b = line.split(';')
        a = a.split(',')
        b = b.split(',')
        print(','.join([x for x in a if x in b]))

lines.close()
 
