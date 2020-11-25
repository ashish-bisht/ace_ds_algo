grid = grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


def number_of_islands(grid):

    if not grid:
        return 0
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            if grid[row][col] == "1":
                count += 1
                dfs(grid, row, col)

    return count


def dfs(grid, row, col):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
        return

    grid[row][col] = "#"

    dfs(grid, row-1, col)
    dfs(grid, row+1, col)
    dfs(grid, row, col-1)
    dfs(grid, row, col+1)


print(number_of_islands(grid))
print(number_of_islands(grid1))
