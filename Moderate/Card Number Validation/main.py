import sys

def doubleNumber(x):
    x *= 2
    if x > 9:
        return int(str(x)[0]) + int(str(x)[1])
    return x

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers = [int(x) for x in line if x != ' ']
        doubled = [doubleNumber(numbers[i]) for i in range(len(numbers) - 2, -1, -2)]
        normal = [numbers[i] for i in range(len(numbers) - 1, -1, -2)]
        print(1 if (sum(normal + doubled) % 10) == 0 else 0)

lines.close()
