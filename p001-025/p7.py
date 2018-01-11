# Project Euler
# Alex Johnson
# Problem 7: 10001st prime number

def prime():
    primes = []
    prime = 2
    while True:
        is_prime = True
        for p in primes:
            if prime % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(prime)
            yield prime
        prime += 1

pgen = prime()
for i in range(10001):
    p = next(pgen)

print(p)
