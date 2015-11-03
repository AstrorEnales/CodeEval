import sys
import re

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        chars = [match.start() for match in re.finditer('[a-zA-Z]', line)]
        isupper = True
        for i in chars:
            c = line[i].upper() if isupper else line[i].lower()
            line = line[0:i] + c + line[i + 1::]
            isupper = isupper == False
        print(line)

lines.close()
