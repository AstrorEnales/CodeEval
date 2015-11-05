import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        n, m = [int(x) for x in line.split(',')]
        primes = set([2])
        num = 3
        while num <= m:
            if all(num % i != 0 for i in primes):
               primes = set(list(primes) + [num])
            num = num + 1
        primes = sorted(list(primes))
        print(len([x for x in primes if x >= n and x <= m]))

lines.close()
