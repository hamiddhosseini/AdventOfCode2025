
from typing import List

def load_grid_from_file(file_name: str) -> List[List[int]]:
    with open(file_name) as f:
        lines = f.read().splitlines()
    grid = [[
        1 if c == '@' else 0 for c in line
    ] for line in lines]

    return grid

def count_and_remove_accessible_rolls(grid):
    accessible_rolls = 0
    grid_copy = [row[:] for row in grid]
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid[row][col] == 1:
                count = count_neigbours(grid, row, col) - 1  # Remove the cell itself
                if count < 4:
                    accessible_rolls += 1
                    grid_copy[row][col] = 9

    if accessible_rolls == 0:
        return accessible_rolls

    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            if grid_copy[row][col] == 9:
                grid[row][col] = 0

    return accessible_rolls + count_and_remove_accessible_rolls(grid)

def count_neigbours(grid: List[List[int]], row:int, col:int) -> int:
    """
    Counts the number of neighbours of a cell in the grid. Neighbours are defined as the 8 cells surrounding the cell, including diagonals.
    """
    min_col = max(0, col - 1)
    max_col = min(len(grid[row]) - 1, col + 1)
    min_row = max(0, row - 1)
    max_row = min(len(grid) - 1, row + 1)
    count = 0
    for c in range(min_col, max_col + 1):
        for r in range(min_row, max_row + 1):
            if grid[r][c] == 1:
                count += 1
    return count

grid = load_grid_from_file('input_final.txt')
count_and_remove_accessible_rolls(grid)