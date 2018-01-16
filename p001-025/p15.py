# Project Euler
# Alex Johnson
# Problem 15: Lattice paths

import math

def choose(n, r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

grid_size = 20
print(choose(grid_size * 2, grid_size))
