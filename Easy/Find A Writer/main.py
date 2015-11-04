import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split('| ')
        indices = [int(x) for x in parts[1].split(' ')]
        print(''.join([parts[0][x - 1] for x in indices]))

lines.close()
