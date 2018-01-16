# Project Euler
# Alex Johnson
# Problem 14: Longest Collatz sequence

def collatz(n):
    count = 1
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3 + 1
    return count

n = 0
max_chain = 0
for i in range(2, 1000000):
    chain = collatz(i)
    if chain > max_chain:
        max_chain = chain
        n = i

print(n)
