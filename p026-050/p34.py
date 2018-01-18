# Project Euler
# Alex Johnson
# Problem 34: Digit factorials

def fac(n):
    prod = 1
    while n > 1:
        prod *= n
        n -= 1
    return prod

def digfac(n):
    total = 0
    for d in str(n):
        total += fac(int(d))
    return total

total = 0
i = 10
s = digfac(i)
while i < 50000:
    if s == i:
        total += i
    i += 1
    s = digfac(i)

print(total)
