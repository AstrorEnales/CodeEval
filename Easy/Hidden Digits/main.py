import sys
import re

lookup = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def indexOfLookupOrSelf(x):
    try:
        return lookup.index(x)
    except:
        return x

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        result = [line[match.start()] for match in re.finditer('[a-j0-9]', line)]
        result = [indexOfLookupOrSelf(x) for x in result]
        print(''.join([str(x) for x in result]) if len(result) > 0 else 'NONE')

lines.close()
