import sys
import math

primes = set([2])
num = 3
while num < 1000:
    if all(num % i != 0 for i in primes):
       primes = set(list(primes) + [num])
    num = num + 1

def isPalindrome(x):
    text = str(x)
    halfLength = len(text) / 2
    offset = len(text) % 2
    return text[0:halfLength][::-1] == text[(halfLength + offset)::]

primes = sorted([x for x in primes if isPalindrome(x)])[::-1]
print(primes[0])