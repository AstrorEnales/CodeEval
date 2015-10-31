import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split(' ')
        maxLen = 0
        maxPart = ''
        for part in parts:
            if len(part) > maxLen:
                maxLen = len(part)
                maxPart = part
        print(maxPart)

lines.close()
