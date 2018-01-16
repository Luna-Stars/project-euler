# Project Euler
# Alex Johnson
# Problem 18: Maximum path sum 1

# read triangle
with open('files/p18-triangle.txt', 'r') as infile:
    triangle = [[int(y) for y in x.strip().split()] for x in infile]

for i in range(len(triangle) - 2, -1, -1):
    prev_row = triangle[i+1]
    for j in range(len(triangle[i])):
        a, b, c = triangle[i][j], prev_row[j], prev_row[j+1]
        triangle[i][j] = max(a+b, a+c)
    del triangle[i+1]

print(triangle[0][0])
