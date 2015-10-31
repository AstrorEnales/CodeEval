import sys
import re
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        print(''.join(re.findall(r'(.)\1*', line)))

lines.close()
 
