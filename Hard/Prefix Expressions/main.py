import sys

def partIsOp(x):
    return x == '+' or x == '/' or x == '*'

def evaluate(op, a, b):
    if op == '+':
        return a + b
    if op == '*':
        return a * b
    if op == '/':
        return a / b

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        parts = [x if partIsOp(x) else float(x) for x in line.split(' ')]
        while len(parts) > 1:
            for i in range(len(parts) - 1, -1, -1):
                if partIsOp(parts[i]):
                    result = evaluate(parts[i], parts[i + 1], parts[i + 2])
                    parts = parts[0:i] + [result] + parts[i + 3::]
                    break
        print(int(parts[0]))

lines.close()
