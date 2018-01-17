# Project Euler
# Alex Johnson
# Problem 23: Non-abundant sums

def sum_facs(x):
    total = 0
    for i in range(1,x):
        if x % i == 0:
            total += i
    return total

abundant = []
for i in range(2, 28124):
    if sum_facs(i) > i:
        abundant.append(i)

vals = list(range(28124))

for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        if abundant[i] + abundant[j] > 28123: break
        vals[abundant[i] + abundant[j]] = 0

print(sum(vals))
