import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = [[int(y) for y in x.split(' ')] for x in line.split(' | ')]
        columns = [tuple(parts[j][i] for j in range(len(parts))) for i in range(len(parts))]
        columns = sorted(columns)
        rows = [' '.join(str(columns[j][i]) for j in range(len(parts))) for i in range(len(parts))]
        print(' | '.join(rows))

lines.close()
