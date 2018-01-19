# Project Euler
# Alex Johnson
# Problem 40: Champernowne's constant

d = ""
i = 1
while len(d) < 1000000:
    d += str(i)
    i += 1

product = 1
for i in [0, 9, 99, 999, 9999, 99999, 999999]:
     product *= int(d[i])

print(product)
