# Project Euler
# Alex Johnson
# Problem 10: Summation of primes

sieve = list(range(2, 2000000))

for i in range(len(sieve)):
    key = sieve[i]
    if key != -1:
        j = i + key
        while j < len(sieve):
            sieve[j] = -1
            j += key

sieve = [x for x in sieve if x != -1]
print(sum(sieve))
