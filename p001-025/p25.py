# Project Euler
# Alex Johnson
# Problem 25: 1000-digit Fibonacci number

prev_fib = 1
fib = 1
i = 2

while len(str(fib)) < 1000:
    temp = fib
    fib = fib+prev_fib
    prev_fib = temp
    i += 1

print(i)
