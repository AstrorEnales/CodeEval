import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        num = int(line)
        print(num == sum([int(x) ** len(line) for x in line]))

lines.close()
