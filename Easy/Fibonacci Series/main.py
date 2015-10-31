import sys

def f(n):
  return n if n < 2 else f(n - 1) + f(n - 2)

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        n = int(line)
        print(f(n))

lines.close()
