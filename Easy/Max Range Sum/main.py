import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        days, values = line.split(';')
        daysNum = int(days)
        valuesNum = [int(x) for x in values.split(' ')]
        gain = max([sum(valuesNum[i:i + daysNum]) for i in range(len(valuesNum) - daysNum + 1)])
        print(gain if gain >= 0 else '0')

lines.close()
 
