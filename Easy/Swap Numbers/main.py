import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split(' ')
        for i in range(len(parts)):
            part = parts[i]
            prefix = part[0]
            suffix = part[len(part) - 1]
            parts[i] = suffix + part[1:len(part) - 1] + prefix
        print(' '.join(parts))

lines.close()
