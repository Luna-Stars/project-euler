# Project Euler
# Alex Johnson
# Problem 48: Self powers

def digits(n):
    for k in range(1, n + 1):
        yield k ** k

print(str(sum(digits(1000)))[-10:])
