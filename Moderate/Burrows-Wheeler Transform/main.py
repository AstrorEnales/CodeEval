import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        line = line[0:len(line) - 1]
        s = sorted([[line[i], i] for i in range(len(line))], key=lambda x: x[0])
        startIndex = line.index('$')
        result = s[startIndex][0]
        index = startIndex
        while len(result) < len(line):
            index = s[index][1]
            result += s[index][0]
        print(result)
        

lines.close()
