# Project Euler
# Alex Johnson
# Problem 9: Special Pythagorean triplet

import sys

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - (b+a)
        if (a**2) + (b**2) == (c**2):
            print(a*b*c)
            sys.exit(0)
