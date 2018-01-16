# Project Euler
# Alex Johnson
# Problem 19: Counting Sundays

import calendar

count = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        if calendar.weekday(y, m, 1) == 6: count += 1

print(count)
