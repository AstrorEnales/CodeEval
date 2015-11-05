import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        n = int(line)
        primes = set([2])
        num = 3
        while num < n:
            if all(num % i != 0 for i in primes):
               primes = set(list(primes) + [num])
            num = num + 1
        primes = sorted(list(primes))
        print(','.join([str(x) for x in primes]))

lines.close()
