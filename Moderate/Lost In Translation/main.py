import sys

map = {'y': 'a',
       'n': 'b',
       'f': 'c',
       'i': 'd',
       'c': 'e',
       'w': 'f',
       'l': 'g',
       'b': 'h',
       'k': 'i',
       'u': 'j',
       'o': 'k',
       'm': 'l',
       'x': 'm',
       's': 'n',
       'e': 'o',
       'v': 'p',
       'z': 'q',
       'p': 'r',
       'd': 's',
       'r': 't',
       'j': 'u',
       'g': 'v',
       't': 'w',
       'h': 'x',
       'a': 'y',
       'q': 'z'}

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        print(' '.join([''.join([map[y] for y in x]) for x in line.split(' ')]))

lines.close()
