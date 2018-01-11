# Project Euler
# Alex Johnson
# Problem 4: Largest palindrome product

def palindrome(n):
    return str(n) == str(n)[::-1]

maxpal = 0

for i in range(100, 1000):
    for j in range(i, 1000):
        if palindrome(i*j) and i*j > maxpal:
            maxpal = i*j

print(maxpal)
