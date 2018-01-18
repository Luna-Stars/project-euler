# Project Euler
# Alex Johnson
# Problem 26: Reciprocal cycles

# sequence A051626 from integer sequence encyclopedia

def isA003592(n):
    while n % 2 == 0:
        n = n // 2
    while n % 5 == 0:
        n = n // 5
    return n == 1

def A051626(n):
    if isA003592(n):
        return 0
    else:
        lpow=1
        while True:
            for mpow in range(lpow-1, -1, -1):
                if (10**lpow-10**mpow) % n == 0:
                    return lpow-mpow
            lpow += 1 # Kenneth Myers, May 06 2016

cycles = [A051626(n) for n in range(1, 1000)]
print(cycles.index(max(cycles)) + 1)
