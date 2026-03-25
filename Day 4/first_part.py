
file_name = 'input2.txt'
with open(file_name) as f:
    lines = f.read().splitlines()

# TODO: Check grid
grid = [[
    1 if c == '@' else 0 for c in line
] for line in lines]

# for line in grid:
#     print(line)

result = [[0 for _ in line] for line in grid]
unaccessible_rolls = 0
accessible_rolls = 0
for row in range(0, len(grid)):
    for col in range(0, len(grid[row])):
        if grid[row][col] == 1:
            min_col = max(0, col - 1)
            max_col = min(len(grid[row]) - 1, col + 1)
            min_row = max(0, row - 1)
            max_row = min(len(grid) - 1, row + 1)
            count = 0
            # print('-----------------------------')
            # print(f'Checking cell ({row}, {col}) with neighbors from ({min_row}, {min_col}) to ({max_row}, {max_col})')
            # for i in range(min_row, max_row + 1):
            #     print(grid[i][min_col:max_col + 1])
            for c in range(min_col, max_col + 1):
                for r in range(min_row, max_row + 1):
                    if grid[r][c] == 1:
                        count += 1
            # print(f'Cell ({row}, {col}) has {count} neighbors')
            if count > 4:
                # print(f'Found an unaccessable roll at ({row}, {col}) with {count} neighbors')
                result[row][col] = 9
                unaccessible_rolls += 1
            else:
                accessible_rolls += 1
                result[row][col] = grid[row][col]

print(f'Unaccessible rolls: {unaccessible_rolls}')
print(f'Accessible rolls: {accessible_rolls}')

# for line in result:
#     print(line)
