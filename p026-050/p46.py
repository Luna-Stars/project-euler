# Project Euler
# Alex Johnson
# Problem 46: Goldbach's other conjecture

import math

# prime sieve
def primesBelow(n):
    primeList = list(range(2, n+1))
    for i in range(len(primeList)):
        if primeList[i] != 0:
            for j in range(i + primeList[i], len(primeList), primeList[i]):
                primeList[j] = 0
    return [p for p in primeList if p != 0]

def isSquare(n):
    return int(math.sqrt(n))**2 == n

n = 35
while True:
    primes = primesBelow(n)
    if primes[-1] != n:
        found = False
        for prime in primes:
            if (n - prime) % 2 != 0: continue
            potential_square = (n - prime) // 2
            if isSquare(potential_square):
                found = True
                break
        if found == False:
            break
    n += 2

print(n)
