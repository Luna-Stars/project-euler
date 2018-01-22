# Project Euler
# Alex Johnson
# Problem 44: Pentagon numbers

import sys

pentagonals = [1]

def genNextPentagonal():
    n = len(pentagonals) + 1
    pentagonals.append((n * (3*n - 1))//2)

def isPentagonal(n):
    while pentagonals[-1] < n:
        genNextPentagonal()
    return n in pentagonals

def getPentagonal(n):
    while n > len(pentagonals):
        genNextPentagonal()
    return pentagonals[n - 1]

i = 2
while True:
    for h in range(i - 1, 0, -1):
        j = getPentagonal(i)
        k = getPentagonal(h)
        if not isPentagonal(j + k): continue
        if not isPentagonal(j - k): continue
        print(j - k)
        sys.exit(0)
    i += 1
