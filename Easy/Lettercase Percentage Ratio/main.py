import sys
import re
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        matchesLower = [match.start() for match in re.finditer('[a-z]', line)]
        matchesUpper = [match.start() for match in re.finditer('[A-Z]', line)]
        matchesLowerPercentage = len(matchesLower) / float(len(line)) * 100.0
        matchesUpperPercentage = len(matchesUpper) / float(len(line)) * 100.0
        print('lowercase: %0.2f uppercase: %0.2f' % (matchesLowerPercentage, matchesUpperPercentage))

lines.close()
