import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        n, m = [int(x) for x in line.split(' ')]
        doors = [False] * n
        for i in range(0, m - 1):
            for j in range(1, len(doors), 2):
                doors[j] = True
            for j in range(2, len(doors), 3):
                doors[j] = doors[j] == False
        doors[-1] = doors[-1] == False
        print(len([x for x in doors if x == False]))

lines.close()

