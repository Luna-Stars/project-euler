# Project Euler
# Alex Johnson
# Problem 30: Digit fifth powers

def sum_fifth(n):
    return sum([int(x) ** 5 for x in str(n)])

total = 0
for i in range(2, 354295):
    if i == sum_fifth(i):
        total += i

print(total)
