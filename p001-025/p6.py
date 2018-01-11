# Project Euler
# Alex Johnson
# Problem 6

squares = 0
ssum = 0

for i in range(1, 101):
    squares += i**2
    ssum += i

ssum *= ssum

print(abs(squares-ssum))
