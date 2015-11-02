import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers, actions = line.split(' : ')
        numbers = numbers.split(' ')
        actions = actions.split(', ')
        for action in actions:
            a, b = [int(x) for x in action.split('-')]
            copy = numbers[b]
            numbers[b] = numbers[a]
            numbers[a] = copy
        print(' '.join(numbers))

lines.close()
