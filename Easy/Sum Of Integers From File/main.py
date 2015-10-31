import sys
lines = open(sys.argv[1], 'r')
sum = 0
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        sum = sum + int(line)
print(sum)

lines.close()
