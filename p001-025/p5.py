# Project Euler
# Alex Johnson
# Problem 5: Smallest multiple

def gcd(a, b):
    if a == 0: return b
    if b == 0: return a
    return gcd(b, a%b)

num = 1
for i in range(20, 1, -1):
    if num % i != 0:
        num *= (i//gcd(num, i))

print(num)
