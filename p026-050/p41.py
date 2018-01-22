# Project Euler
# Alex Johnson
# Problem 41: Pandigital Prime

from itertools import permutations

# only pandigital #s that can be primes are 4-digit and 7-digit pandigitals
primecache = []

def prime(a):
    if a in primecache: return True
    if a <= 1: return False
    for i in range(2, a//2 + 1):
        if a % i == 0: return False
    primecache.append(a)
    return True

# solution
pandigital7s = [int(''.join(p)) for p in permutations('1234567')]
pandigital7s.sort()
pandigital7s.reverse()

for num in pandigital7s:
    if prime(num):
        print(num)
        break
