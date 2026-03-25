# Day 4: Printing Department

This puzzle uses a grid made of two characters:
- `@` means occupied
- `.` means empty

Each script converts the grid into 1/0 values and checks the 8-neighborhood (including diagonals) for every occupied cell.

## Part 1

`first_part.py` counts how many occupied cells are accessible.

A cell is considered accessible when it has fewer than 4 occupied neighbors.
This is computed in one pass on the original grid.

## Part 2

`second_part.py` repeatedly removes accessible occupied cells until no more can be removed.

At each round:
1. Find all currently accessible cells
2. Remove them together
3. Repeat

The final result is the total number of removed cells across all rounds.
