import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        print(len([x for x in '{0:b}'.format(int(line)) if x == '1']))

lines.close()
