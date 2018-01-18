# Project Euler
# Alex Johnson
# Problem 36: Double-base palindromes

def palindrome(x): return x == x[::-1]

total = 0
for i in range(1, 1000000):
    if palindrome(str(i)) and palindrome(bin(i)[2:]):
        total += i

print(total)
