import sys

count = -1
result = []
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        if count == -1:
            count = int(line)
        else:
            result.append(line)

lines.close()

result = sorted(result, key=lambda x:len(x))[::-1]
for i in range(count):
    print(result[i])
