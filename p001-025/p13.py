# Project Euler
# Alex Johnson
# Problem 13: Large sum

with open('files/p13-nums.txt', 'r') as infile:
    nums = [int(x.strip()) for x in infile]

print(str(sum(nums))[:10])
