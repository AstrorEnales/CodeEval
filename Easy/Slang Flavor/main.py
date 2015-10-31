import sys
import re
from itertools import cycle

slang = cycle([', yeah!', ', this is crazy, I tell ya.', ', can U believe this?', ', eh?', ', aw yea.', ', yo.', '? No way!', '. Awesome!'])
count = 0
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        indices = [match.start() for match in re.finditer('(\.|!|\?)', line)]
        startAt = 1 if count % 2 == 0 else 0
        count = count + len(indices)
        indices = indices[startAt::2]
        slangSelected = [next(slang) for x in indices]
        for i in range(len(indices)):
            index = len(indices) - i - 1
            punctuationIndex = indices[index]
            line = line[0:punctuationIndex] + slangSelected[index] + line[(punctuationIndex + 1)::]
        print(line)

lines.close()
