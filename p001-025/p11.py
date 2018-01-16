# Project Euler
# Alex Johnson
# Problem 11: Largest product in a grid

# load grid
with open("files/p11-grid.txt", "r") as infile:
    grid = [[int(y) for y in x.strip().split()] for x in infile]

products = []
for i in range(len(grid)):
    for j in range(len(grid[i])):
        try:
            products.append(grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]) # horiz product
            products.append(grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]) # vert product
            products.append(grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]) # diag product
            products.append(grid[i+3][j] * grid[i+2][j+1] * grid[i+1][j+2] * grid[i][j+3]) # other diag
        except:
            break

print(max(products))
