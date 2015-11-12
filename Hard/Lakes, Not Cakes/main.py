import sys

def floodfill(field, i, j, index):
    upperLimitY = len(field) - 1
    upperLimitX = len(field[0]) - 1
    
    if i > 0 and field[i - 1][j] == 'o':
        field[i - 1][j] = index
        field = floodfill(field, i - 1, j, index)
    if i < upperLimitY and field[i + 1][j] == 'o':
        field[i + 1][j] = index
        field = floodfill(field, i + 1, j, index)
    if j > 0 and field[i][j - 1] == 'o':
        field[i][j - 1] = index
        field = floodfill(field, i, j - 1, index)
    if j < upperLimitX and field[i][j + 1] == 'o':
        field[i][j + 1] = index
        field = floodfill(field, i, j + 1, index)
    
    if i > 0:
        if j > 0 and field[i - 1][j - 1] == 'o':
            field[i - 1][j - 1] = index
            field = floodfill(field, i - 1, j - 1, index)
        if j < upperLimitX and field[i - 1][j + 1] == 'o':
            field[i - 1][j + 1] = index
            field = floodfill(field, i - 1, j + 1, index)
    
    if i < upperLimitY:
        if j > 0 and field[i + 1][j - 1] == 'o':
            field[i + 1][j - 1] = index
            field = floodfill(field, i + 1, j - 1, index)
        if j < upperLimitX and field[i + 1][j + 1] == 'o':
            field[i + 1][j + 1] = index
            field = floodfill(field, i + 1, j + 1, index)
    return field

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        field = [x.split(' ') for x in line.split(' | ')]
        index = 1
        for i in range(len(field)):
            for j in range(len(field[0])):
                if field[i][j] == 'o':
                    field[i][j] = index
                    field = floodfill(field, i, j, index)
                    index += 1
        print(index - 1)

lines.close()

