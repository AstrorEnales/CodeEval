import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        number, pattern = line.split(' ')
        indexOfPlus = pattern.find('+')
        indexOfMinus = pattern.find('-')
        if indexOfPlus >= 0:
            a = int(number[0:indexOfPlus])
            b = int(number[indexOfPlus::])
            print(a + b)
        else:
            a = int(number[0:indexOfMinus])
            b = int(number[indexOfMinus::])
            print(a - b)

lines.close()
