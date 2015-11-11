import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        n, numbers = line.split(';')
        n = int(n)
        numbers = [int(x) for x in numbers.split(',')]
        lookup = [0] * n
        for num in numbers:
            lookup[num] += 1
            if lookup[num] >= 2:
                print(num)
                break

lines.close()
