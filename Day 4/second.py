
file_name = 'input2.txt'
with open(file_name) as f:
    lines = f.read().splitlines()

# TODO: Check grid
grid = [[
    1 if c == '@' else 0 for c in line
] for line in lines]


def count_and_remove_accessible_rolls(grid):
    accessible_rolls = 0
    grid_copy = [row[:] for row in grid]
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid[row][col] == 1:
                min_col = max(0, col - 1)
                max_col = min(len(grid[row]) - 1, col + 1)
                min_row = max(0, row - 1)
                max_row = min(len(grid) - 1, row + 1)
                count = 0
                for c in range(min_col, max_col + 1):
                    for r in range(min_row, max_row + 1):
                        if grid[r][c] == 1:
                            count += 1
                if count <= 4:
                    accessible_rolls += 1
                    grid_copy[row][col] = 9

    if accessible_rolls == 0:
        return accessible_rolls

    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid_copy[row][col] == 9:
                grid[row][col] = 0

    # print(f'Accessible rolls found in this iteration: {accessible_rolls}')
    return accessible_rolls + count_and_remove_accessible_rolls(grid)

count_and_remove_accessible_rolls(grid)