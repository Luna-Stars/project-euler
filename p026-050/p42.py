# Project Euler
# Alex Johnson
# Problem 42: Coded triangle numbers

# step 1: load words
with open("files/p42-words.txt", "r") as infile:
    words = infile.readline().strip().replace("\"", "").split(",")

# step 2: calculate scores
for i in range(len(words)):
    word = words[i]
    total = 0
    for char in word:
        total += ord(char) - ord('A') + 1
    words[i] = total

# step 3: calculate triangle numbers as necessary
nums = [1]
while nums[-1] < max(words):
    n = len(nums) + 1
    nums.append((n * (n + 1)) // 2)

# step 4: count
count = 0
for word in words:
    if word in nums:
        count += 1

print(count)
