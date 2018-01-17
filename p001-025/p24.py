# Project Euler
# Alex Johnson
# Problem 24: Lexicographic permutations

import itertools

digits = list(str(x) for x in range(10))
print("".join(list(itertools.permutations(digits))[999999]))
