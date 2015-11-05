import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        words, chars = line.split(', ')
        chars = list(chars)
        for i in range(len(words) - 1, -1, -1):
            if words[i] in chars:
                words = words[0:i] + words[(i + 1)::]
        print(words)

lines.close()
