import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        if len(line) <= 55:
            print(line)
        else:
            parts = line.split(' ')
            length = 0
            i = 0
            for part in parts:
                if length + len(part) >= 40:
                    break
                length = length + len(part) + 1
                i = i + 1
            if i == 0:
                print(parts[0][0:40] + '... <Read More>')
            else:
                print(' '.join(parts[0:i]) + '... <Read More>')

lines.close()
 
