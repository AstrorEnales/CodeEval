import sys
import re

digitLines = [['-**--', '--*--', '***--', '***--', '-*---', '****-', '-**--', '****-', '-**--', '-**--'],
              ['*--*-', '-**--', '---*-', '---*-', '*--*-', '*----', '*----', '---*-', '*--*-', '*--*-'],
              ['*--*-', '--*--', '-**--', '-**--', '****-', '***--', '***--', '--*--', '-**--', '-***-'],
              ['*--*-', '--*--', '*----', '---*-', '---*-', '---*-', '*--*-', '-*---', '*--*-', '---*-'],
              ['-**--', '-***-', '****-', '***--', '---*-', '***--', '-**--', '-*---', '-**--', '-**--'],
              ['-----', '-----', '-----', '-----', '-----', '-----', '-----', '-----', '-----', '-----']]

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        digits = [int(line[match.start()]) for match in re.finditer('[0-9]', line)]
        for digitLine in digitLines:
            print(''.join([digitLine[i] for i in digits]))

lines.close()