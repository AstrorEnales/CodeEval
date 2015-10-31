import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        print('1' if (int(line) % 2) == 0 else '0')

lines.close()
 
