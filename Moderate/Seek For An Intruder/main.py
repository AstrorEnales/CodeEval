import sys
import re
from collections import Counter

def dottedToDottedDecimal(x, base):
    return '.'.join([str(int(y, base)) for y in x.split('.')])

def isInRange(x):
    parts = [int(y) for y in x.split('.')]
    if len(parts) != 4:
        return False
    return parts[0] >= 1 and parts[0] <= 255 and parts[1] >= 0 and parts[1] <= 255 and parts[1] >= 0 and parts[1] <= 255 and parts[1] >= 0 and parts[1] <= 254

adresses = []
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        # Hexadecimal
        dottedHexadecimal = re.findall('0x[0-9a-f]{1,2}\.0x[0-9a-f]{1,2}\.0x[0-9a-f]{1,2}\.0x[0-9a-f]{1,2}', line)
        dottedHexadecimal.extend(['.'.join(['0x' + x[i:(i + 2)] for i in range(2, len(x), 2)]) for x in re.findall('0x[0-9a-f]{8}', line)])
        # Octal
        dottedOctal = re.findall('0[0-7]{3}\.0[0-7]{3}\.0[0-7]{3}\.0[0-7]{3}', line)
        # Binary
        dottedBinary = re.findall('[01]{8}\.[01]{8}\.[01]{8}\.[01]{8}', line)
        dottedBinary.extend(['.'.join([x[i:(i + 8)] for i in range(0, len(x), 8)]) for x in re.findall('[01]{32}', line)])
        decimal = ['{0:032b}'.format(int(x)) for x in re.findall('[0-9]{1,11}', line)]
        octal = ['{0:032b}'.format(int(x, 8)) for x in re.findall('[0-7]{1,12}', line)]
        dottedBinary.extend(['.'.join([x[i:(i + 8)] for i in range(0, len(x), 8)]) for x in decimal])
        dottedBinary.extend(['.'.join([x[i:(i + 8)] for i in range(0, len(x), 8)]) for x in octal])
        # Decimal
        dottedDecimal = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', line)
        dottedDecimal.extend([dottedToDottedDecimal(x, 16) for x in dottedHexadecimal])
        dottedDecimal.extend([dottedToDottedDecimal(x, 8) for x in dottedOctal])
        dottedDecimal.extend([dottedToDottedDecimal(x, 2) for x in dottedBinary])
        
        adresses.extend([x for x in dottedDecimal if isInRange(x)])

lines.close()

print(sorted(Counter(adresses).items(), key=lambda x: x[1])[-1][0])