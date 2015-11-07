import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        depth = int(line)
        result = [1]
        current = [1]
        for i in range(1, depth):
            current = [1] + [current[j] + current[j + 1] for j in range(len(current) - 1)] + [1]
            result.extend(current)
        print(' '.join([str(x) for x in result]))

lines.close()
