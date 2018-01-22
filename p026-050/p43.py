# Project Euler
# Alex Johnson
# Problem 43: Pandigital numbers

from itertools import permutations

pandigital9s = [int(''.join(x)) for x in permutations('0123456789')]
pandigital9s.sort()

total = 0
for pan in pandigital9s:
    pan_digits = str(pan)
    if int(pan_digits[1:4]) % 2 != 0:
        continue
    elif int(pan_digits[2:5]) % 3 != 0:
        continue
    elif int(pan_digits[3:6]) % 5 != 0:
        continue
    elif int(pan_digits[4:7]) % 7 != 0:
        continue
    elif int(pan_digits[5:8]) % 11 != 0:
        continue
    elif int(pan_digits[6:9]) % 13 != 0:
        continue
    elif int(pan_digits[7:10]) % 17 != 0:
        continue
    total += pan

print(total)
