# Project Euler
# Alex Johnson
# Problem 39: Integer right triangles

resultp = 0
resultsols = 0

for p in range(2, 1001, 2):
    sols = 0
    for a in range(2, p//3 + 1):
        if ((p * (p - 2.0*a)) % (2.0*(p - a))) == 0:
            sols += 1
    if sols > resultsols:
        resultp, resultsols = p, sols

print(resultp)
