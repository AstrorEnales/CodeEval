import sys

def isSquare(parts, x, y, n):
    a = y * 5 + x
    b = a + n
    c = a + 5 * n
    # top line
    for i in [[a + x, a + 1 + x] for x in range(0, n)]:
        if i not in parts and i[::-1] not in parts:
            return False
    # bottom line
    for i in [[c + x, c + 1 + x] for x in range(0, n)]:
        if i not in parts and i[::-1] not in parts:
            return False
    # left line
    for i in [[a + x * 5, a + 5 + x * 5] for x in range(0, n)]:
        if i not in parts and i[::-1] not in parts:
            return False
    # right line
    for i in [[b + x * 5, b + 5 + x * 5] for x in range(0, n)]:
        if i not in parts and i[::-1] not in parts:
            return False
    return True

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = [[int(y) for y in x.split(' ')] for x in line.split(' | ')]
        result = 0
        for n in range(1, 5):
            for x in range(1, 6 - n):
                for y in range(0, 6 - n - 1):
                    if isSquare(parts, x, y, n):
                        result += 1
        print(result)

lines.close()
