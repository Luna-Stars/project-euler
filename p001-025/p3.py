# Project Euler
# Alex Johnson
# Problem 3: Largest prime factor

import math

num = 600851475143

facs = []
for i in range(2, int(math.sqrt(num))):
    if num % i == 0:
        prime = True
        for f in facs:
            if i % f == 0:
                prime = False
        if prime:
            facs.append(i)

print(facs[-1])
