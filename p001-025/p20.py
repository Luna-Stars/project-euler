# Project Euler
# Alex Johnson
# Problem 20: Factorial digit sum

n = 100
factorial = 1

for i in range(n, 1, -1):
    factorial *= i

print(sum([int(x) for x in str(factorial)]))
