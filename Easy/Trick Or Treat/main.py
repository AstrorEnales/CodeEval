import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = line.split(', ')
        data = {}
        for part in parts:
            subparts = part.split(': ')
            data[subparts[0]] = int(subparts[1])
        candy = data['Houses'] * (data['Vampires'] * 3 + data['Zombies'] * 4 + data['Witches'] * 5)
        print(candy / (data['Vampires'] + data['Zombies'] + data['Witches']))

lines.close()
