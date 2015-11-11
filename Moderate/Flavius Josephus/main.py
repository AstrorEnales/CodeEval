import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        n, step = [int(x) for x in line.split(',')]
        circle = {i: True for i in range(0, n)}
        dead = []
        current = 0
        while len(dead) < n:
            offset = -1
            living = 0
            while living < step:
                offset += 1
                if circle[(current + offset) % n]:
                    living += 1
            current = (current + offset) % n
            dead.append(current)
            circle[current] = False
        print(' '.join([str(x) for x in dead]))

lines.close()
