import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        words = line.split(' ')
        print(words[len(words) - 2])

lines.close()
