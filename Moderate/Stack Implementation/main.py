import sys

def push(stack, e):
    stack.append(e)
    return stack

def pop(stack):
    if len(stack) == 0:
        return stack, None
    e = stack[-1]
    stack = stack[0:(len(stack) - 1)]
    return stack, e

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers = line.split(' ')
        result = []
        stack = []
        for i in numbers:
            stack = push(stack, i)
        while(len(stack) >= 1):
            stack, e = pop(stack)
            result.append(e)
            stack, e = pop(stack)
        print(' '.join(result))

lines.close()
