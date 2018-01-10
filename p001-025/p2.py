# Project Euler
# Alex Johnson
# Problem 2: Even Fibonacci numbers

def fib():
    fibs = [1, 1]
    next_fib = fibs[-1] + fibs[-2]
    while next_fib <= 4000000:
        fibs.append(next_fib)
        yield next_fib
        next_fib = fibs[-1] + fibs[-2]

print(sum([x for x in fib() if x % 2 == 0]))
