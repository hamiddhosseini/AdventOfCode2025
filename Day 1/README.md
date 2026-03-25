# Day 1: Secret Entrance

## Problem

You are given a series of movement commands (e.g. `L68`, `R30`) along a circular number line. Each command moves a pointer left (`L`) or right (`R`) by a given distance. The pointer wraps around within a fixed range (`min_pointer` to `max_pointer`). Starting from a defined `start_point`, you must count how many times the pointer hits or crosses a specific `count_point`.

In this puzzle the range is `[0, 100]`, the starting position is `50`, and the count point is `0`.

## Part 1

Count how many times the pointer **lands exactly on** the `count_point` after each movement. Wrapping is applied after each step, and only the final resting position is checked.

**Approach:** Apply each movement, wrap the resulting position into the valid range using modular arithmetic, and increment the counter if the position equals `count_point`.

## Part 2

Count how many times the pointer **passes through or lands on** the `count_point` during each movement, including multiple crossings caused by large jumps that wrap around the range more than once.

**Approach:** Before wrapping, determine whether the movement crosses the boundary and how many times. If the movement distance is larger than the range, count full loops. Additionally check for a partial crossing at the boundary in the direction of travel. Finally, check if the wrapped end position lands on `count_point`. A comprehensive set of unit tests (`test_count_passing_times`) is included to verify edge cases such as starting on the count point, exact boundary landings, and multi-loop jumps.
