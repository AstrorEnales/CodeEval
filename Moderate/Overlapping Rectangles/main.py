import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers = [int(x) for x in line.split(',')]
        r1left = min(numbers[0], numbers[2])
        r1right = max(numbers[0], numbers[2])
        r1top = min(numbers[1], numbers[3])
        r1bottom = max(numbers[1], numbers[3])
        r2left = min(numbers[4], numbers[6])
        r2right = max(numbers[4], numbers[6])
        r2top = min(numbers[5], numbers[7])
        r2bottom = max(numbers[5], numbers[7])
        print((r2left > r1right or r2right < r1left or r2top > r1bottom or r2bottom < r1top) == False);

lines.close()
