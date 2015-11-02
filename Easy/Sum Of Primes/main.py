import sys
import math

primes = set([2])
num = 3
while len(primes) < 1000:
    if all(num % i != 0 for i in primes):
       primes = set(list(primes) + [num])
    num = num + 1

print(sum(primes))