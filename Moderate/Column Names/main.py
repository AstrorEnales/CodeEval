import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        x = int(line)
        result = ''
        while x > 0:
            x, i = divmod(x, 26)
            x, i = [x - 1, 26] if i == 0 and x > 0 else [x, i]
            result += chr(ord('A') + i - 1)
        print(result[::-1])

lines.close()
