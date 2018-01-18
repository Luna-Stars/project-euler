# Project Euler
# Alex Johnson
# Problem 27: Quadratic primes

primecache = []

def prime(a):
    if a in primecache: return True
    if a <= 1: return False
    for i in range(2, a//2 + 1):
        if a % i == 0: return False
    primecache.append(a)
    return True

def compute(a, b, n):
    return (n**2) + (a*n) + b

maxprimes = 0
maxcoeffs = (0, 0)

for a in range(-999, 1000):
    for b in range(1001):
        if not prime(b): continue
        n = 0
        count = 0
        while prime(compute(a, b, n)):
            n += 1
            count += 1
        if count > maxprimes:
            maxprimes = count
            maxcoeffs = (a, b)

print(maxcoeffs[0] * maxcoeffs[1])
