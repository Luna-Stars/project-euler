# Project Euler
# Alex Johnson
# Problem 12: Highly divisible triangular number

def divisor_count(n):
    result_set = set()
    for i in range(1, 1+int(n**0.5)):
        if n % i == 0:
            result_set.add(n // i)
            result_set.add(i)
    return len(result_set)

i = 1
n = 1

while divisor_count(n) < 500:
    # next triangle number
    i += 1
    n += i

print(n)
