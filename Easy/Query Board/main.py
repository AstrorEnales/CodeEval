import sys

board = []
for i in range(256):
  board.append(([0] * 256))

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split(' ')
        if parts[0] == 'SetRow':
            board[int(parts[1])] = [int(parts[2])] * 256
        elif parts[0] == 'SetCol':
            for i in range(256):
                board[i][int(parts[1])] = int(parts[2])
        elif parts[0] == 'QueryRow':
            print(sum(board[int(parts[1])]))
        elif parts[0] == 'QueryCol':
            j = int(parts[1])
            print(sum([x[j] for x in board]))

lines.close()
