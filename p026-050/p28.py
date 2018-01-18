# Project Euler
# Alex Johnson
# Problem 28: Number spiral diagonals

spiral_width = 1001
ring_num = spiral_width // 2

total = 1
for i in range(2, ring_num + 1):
    ring_width = i * 2 + 1
    ring_square = ring_width ** 2
    step = ring_width - 1
    for j in range(4):
        total += ring_square
        ring_square -= step

print(total)
