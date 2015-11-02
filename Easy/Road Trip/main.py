import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        distances = sorted([int(x.split(',')[1].replace(';', '')) for x in line.split('; ')])
        current = 0
        result = []
        for i in distances:
            result.append(i - current)
            current = i
        print(','.join([str(x) for x in result]))
        

lines.close()
