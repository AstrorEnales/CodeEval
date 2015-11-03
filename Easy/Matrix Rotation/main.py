import sys
import math

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        elements = line.split(' ')
        n = int(math.sqrt(len(elements)))
        matrix = [elements[i:(i + n)] for i in range(0, len(elements), n)]
        result = []
        for i in range(n):
          for j in range(n):
            result.append(matrix[n - j - 1][i])
        print(' '.join(result))

lines.close()
