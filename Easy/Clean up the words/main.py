import sys
import re
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        line = re.sub('[^a-zA-Z]', ' ', line).strip().lower()
        line = re.sub(' +', ' ', line)
        print(line)

lines.close()
 
