import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        word, pattern = line.split(' ')
        for i in range(len(pattern)):
            insert = word[i].lower() if pattern[i] == '0' else word[i].upper()
            word = word[:i] + insert + word[(i + 1):]
        print(word)

lines.close()
