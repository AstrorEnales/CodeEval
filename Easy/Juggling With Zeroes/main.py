import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split(' ')
        binary = ''.join([(('0' if parts[i * 2] == '0' else '1') * len(parts[i * 2 + 1])) for i in range(int(len(parts) / 2))])
        print(int(binary, 2))

lines.close()
