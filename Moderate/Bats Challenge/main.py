import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = [int(x) for x in line.split(' ')]
        l, d, n = parts[0:3]
        bats = sorted(parts[3:])
        if len(bats) > 0:
            startToFirst = len(range(6, bats[0] - d + 1, d))
            inbetween = sum([len(range(bats[i] + d, bats[i + 1] - d + 1, d)) for i in range(0, len(bats) - 1)])
            lastToEnd = len(range(bats[-1] + d, l - 5, d))
            print(startToFirst + lastToEnd + inbetween)
        else:
            print(len(range(6, l - 5, d)))

lines.close()
