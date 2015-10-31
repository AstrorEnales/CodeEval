import sys
import math

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers = [int(x) for x in line.split(' ')][1::]
        sums = [sum([math.fabs(numbers[i] - numbers[j]) for j in range(len(numbers)) if i != j]) for i in range(len(numbers))]
        print(int(min(sums)))

lines.close()
