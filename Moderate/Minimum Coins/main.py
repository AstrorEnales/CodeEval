import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        n = int(line)
        count = 0
        if n >= 5:
            fit = int(n / 5)
            count += fit
            n -= fit * 5
        if n >= 3:
            fit = int(n / 3)
            count += fit
            n -= fit * 3
        count += n
        print(count)

lines.close()
