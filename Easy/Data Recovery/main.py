import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        text, hints = line.split(';')
        text = text.split(' ')
        hints = [int(x) for x in hints.split(' ')]
        lookup = {}
        for i in range(len(hints)):
            lookup[hints[i]] = text[i]
        print(' '.join([lookup[x] if x in lookup else text[len(text) - 1] for x in range(1, len(text) + 1)]))

lines.close()
