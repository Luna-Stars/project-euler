# Project Euler
# Alex Johnson
# Problem 50: Consecutive Prime Sum

# prime sieve
def primesBelow(n):
    primeList = list(range(2, n+1))
    for i in range(len(primeList)):
        if primeList[i] != 0:
            for j in range(i + primeList[i], len(primeList), primeList[i]):
                primeList[j] = 0
    return [p for p in primeList if p != 0]

primes = primesBelow(1000000)

prime_sums = [0]
for p in primes:
    prime_sums.append(prime_sums[-1] + p)
    if prime_sums[-1] > 1000000: break

prime = 0
terms = 1
for start in range(len(prime_sums)):
    for end in range(len(prime_sums) - 1, start + terms, -1):
        checksum = prime_sums[end] - prime_sums[start]
        if checksum in primes and (end - start) > terms:
            terms = end - start
            prime = checksum

print(prime)
