# Project Euler
# Alex Johnson
# Problem 49: Prime permutations

import itertools

primes = list(range(10000))
primes[1] = 0

for p in primes:
    if p != 0:
        for i in range(p*2, len(primes), p):
            primes[i] = 0

primes = [x for x in primes[1000:] if x != 0]
seqs = []

def isArithmetic(l):
    return (l[1] - l[0]) == (l[2] - l[1])

for p in primes:
    perms = [y for y in [int(''.join(x)) for x in set(itertools.permutations(str(p))) if x[0] != '0'] if y in primes]
    perms.sort()
    if len(perms) >= 3:
        sublists = [x for x in itertools.combinations(perms, 3) if isArithmetic(x) and x not in seqs]
        seqs += sublists

for x in seqs:
    print(''.join(str(y) for y in x))
