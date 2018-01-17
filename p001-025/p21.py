# Project Euler
# Alex Johnson
# Problem 21: Amicable numbers

def sum_facs(x):
    total = 0
    for i in range(1,x):
        if x % i == 0:
            total += i
    return total

sums = [sum_facs(i) for i in range(1, 10000)]
pairs = []

for i in range(len(sums)):
    val = i + 1
    # avoid duplicates
    if sums[i] >= len(sums): continue
    if sums[i] <= i: continue
    if sums[i] == val: continue
    # add the thign
    if sums[sums[i] - 1] == val:
        pair = {val, sums[i]}
        if pair not in pairs:
            pairs.append(pair)

# print result
print(sum([sum(x) for x in pairs]))
