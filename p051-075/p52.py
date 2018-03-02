# Project Euler
# Alex Johnson
# Problem 52: Permuted multiples

def permuted(x, y):
    """Determine if x and y have the same digits"""
    sx, sy = list(str(x)), list(str(y)); sx.sort(); sy.sort()
    return sx == sy

def all_permuted(a, b, c, d, e, f):
    return permuted(a, b) and permuted(b, c) and permuted(c, d) and permuted(d, e) and permuted(e, f)

def is_sol(a):
    return all_permuted(a, a*2, a*3, a*4, a*5, a*6)

curr = 2
while not is_sol(curr): curr += 1

print(curr)
