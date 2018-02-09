# Project Euler
# Alex Johnson
# Problem 47: Distinct primes factors

import math

primes = list(range(100000))
primes[1] = 0
for x in primes:
    if x != 0:
        for i in range(x*2, len(primes), x): primes[i] = 0

primes = [x for x in primes if x != 0]

currentNum = 209
streakCount = 0

def numPrimeFacs(n):
    count = 0
    for p in primes:
        if p > n/2:
            break
        if n % p == 0: count += 1
    return count

while streakCount < 4:
    currentNum += 1
    if numPrimeFacs(currentNum) >= 4:
        streakCount += 1
    else: streakCount = 0

print(currentNum - 3)
