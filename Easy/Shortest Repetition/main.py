import sys
import math

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        shortest = len(line)
        start = len(line)
        for i in range(1, start)[::-1]:
            pattern = line[0:i]
            parts = [line[x:(x + i)] for x in range(0, len(line), i)]
            if all([x == pattern for x in parts]):
                shortest = i
        print(shortest)

lines.close()
