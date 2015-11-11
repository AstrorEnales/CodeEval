import sys

def isPalindrome(x):
    text = str(x)
    halfLength = int(len(text) / 2)
    offset = len(text) % 2
    return text[0:halfLength][::-1] == text[(halfLength + offset)::]

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        x = int(line)
        i = 0
        while isPalindrome(x) == False:
            x += int(str(x)[::-1])
            i += 1
        print('%s %s' % (i, x))

lines.close()
