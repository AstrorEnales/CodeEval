import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split(' ')
        index = len(parts) - 1 - int(parts[-1])
        if index >= 0:
            print(parts[index])

lines.close()
