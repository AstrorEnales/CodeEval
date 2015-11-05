import sys
import re

lines = open(sys.argv[1], 'r')
lastPosition = -1
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        width = len(line)
        passages = {line[match.start()]: match.start() for match in re.finditer('C|_', line)}
        indices = list(passages.values())
        if lastPosition == -1:
            lastPosition = indices[0]
            newPosition = lastPosition
        else:
            target = passages['C' if len(indices) > 1 else '_']
            diff = min(max(target - lastPosition, -1), 1)
            newPosition = lastPosition + diff
        movement = '|' if newPosition == lastPosition else ('/' if newPosition < lastPosition else '\\')
        print(line[0:newPosition] + movement + line[(newPosition + 1)::])
        lastPosition = newPosition

lines.close()
