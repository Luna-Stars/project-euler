# Project Euler
# Alex Johnson
# Problem 45: Triangular, pentagonal, and hexagonal

import math

def isTriangle(n):
    part = n * 2
    lower = int(math.floor(math.sqrt(part)))
    higher = int(math.ceil(math.sqrt(part)))
    if lower * higher == part: return True
    return False

def isPentagonal(n):
    part = (1 + math.sqrt(24*n + 1)) // 6
    pot = (3*part*part - part)//2
    return pot == n

def hexag(n):
    return 2*n*n - n

n = 144
while not (isTriangle(hexag(n)) and isPentagonal(hexag(n))):
    n += 1

print(hexag(n))
