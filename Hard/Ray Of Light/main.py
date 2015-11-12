import sys

def traverse(startx, starty, field, x, y, dx, dy, depth):
    if depth >= 20:
        return field
    x += dx
    y += dy
    depth += 1
    inStartPosition = x == startx and y == starty
    if (x == 0 and y == 0) or (x == 0 and y == 9) or (x == 9 and y == 0) or (x == 9 and y == 9):
        return field
    if (x == 0 or x == 9) and inStartPosition == False:
        dx = -dx
        x += dx
    if (y == 0 or y == 9) and inStartPosition == False:
        dy = -dy
        y += dy
    if field[y][x] == 'o':
        return field
    if field[y][x] == '*':
        depth -= 1
        field = traverse(startx, starty, field, x, y, dx, dy, depth)
        field = traverse(startx, starty, field, x, y, -dx, dy, depth)
        field = traverse(startx, starty, field, x, y, dx, -dy, depth)
    else:
        insert = '/' if (dx == 1 and dy == -1) or (dx == -1 and dy == 1) else '\\'
        field[y][x] = 'X' if field[y][x] == 'X' or (field[y][x] == '/' and insert == '\\') or (field[y][x] == '\\' and insert == '/') else insert
        if inStartPosition == False:
            field = traverse(startx, starty, field, x, y, dx, dy, depth)
    return field

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        field = [list(line[i:(i + 10)]) for i in range(0, len(line), 10)]
        x, y = -1, -1
        for i in range(10):
            for j in range(10):
                if field[j][i] == '/' or field[j][i] == '\\':
                    x, y = i, j
                    break
            if x != -1:
                break
        dx, dy = 1, 1
        if field[y][x] == '/':
            if x == 9 or y == 0:
                dx = -1
            if y == 9 or x == 0:
                dy = -1
        else:
            if x == 9 or y == 9:
                dx = -1
            if y == 9 or x == 9:
                dy = -1
        field = traverse(x, y, field, x, y, dx, dy, 1)
        print(''.join([''.join([x for x in y]) for y in field]))

lines.close()
