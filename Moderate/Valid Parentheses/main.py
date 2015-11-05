import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        stack = []
        result = True
        for x in line:
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
            elif len(stack) == 0 or (stack[-1] == '(' and x != ')') or (stack[-1] == '[' and x != ']') or (stack[-1] == '{' and x != '}'):
                result = False
                break
            else:
                stack = stack[0:(len(stack) - 1)]
        if len(stack) > 0:
            result = False
        print(result)

lines.close()
