import sys

def sumOfSquaredDigits(num):
    return sum([int(x) ** 2 for x in str(num)])

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        num = int(line)
        foundDuplicate = False
        track = [num]
        while num != 1 and foundDuplicate == False:
            num = sumOfSquaredDigits(num)
            foundDuplicate = len([x for x in track if x == num]) > 0
            track.append(num)
        print(1 if num == 1 else 0)

lines.close()
