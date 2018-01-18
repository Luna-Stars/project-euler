# Project Euler
# Alex Johnson
# Problem 35: Circular primes

from progressbar import ProgressBar
pbar = ProgressBar()

with open('files/p35-primes.txt', 'r') as infile:
    primes = [int(x) for x in "".join(infile.readlines()).replace("\n","").replace(" ","").split(",")]

def rotations(n):
    rots = []
    n_str = str(n)
    for i in range(len(n_str)):
        rots.append(int(n_str))
        n_str = n_str[-1] + n_str[:-1]
    return rots

count = 0
for prime in pbar(primes):
    rotation = True
    for rot in rotations(prime):
        if rot not in primes:
            rotation = False
    if rotation: count += 1

print(count)
