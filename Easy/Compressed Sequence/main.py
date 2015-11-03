import sys
import math

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        elements = line.split(' ')
        result = []
        counter = 0
        current = -1
        for i in elements:
          if current != i:
            if current != -1:
              result.append(str(counter))
              result.append(current)
            current = i
            counter = 0
          counter = counter + 1
        if counter > 0:
          result.append(str(counter))
          result.append(current)
        print(' '.join(result))

lines.close()
