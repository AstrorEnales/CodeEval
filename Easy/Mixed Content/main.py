import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers = []
        words = []
        for part in line.split(','):
            if part.isdigit():
                numbers.append(part)
            else:
                words.append(part)
        print(','.join(words) + ('|' if len(words) > 0 and len(numbers) > 0 else '') + ','.join(numbers))

lines.close()
