import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        text, suffix = line.split(',')
        print('1' if text.endswith(suffix) else '0')
        

lines.close()
