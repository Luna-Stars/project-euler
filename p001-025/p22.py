# Project Euler
# Alex Johnson
# Problem 22: Names scorers

with open('files/p22-names.txt', 'r') as infile:
    names = infile.readline().strip().replace("\"", "").split(",")
names.sort()

for i in range(len(names)):
    name_score = sum([ord(x) - 64 for x in list(names[i])])
    name_pos = i + 1
    names[i] = name_score * name_pos

print(sum(names))
