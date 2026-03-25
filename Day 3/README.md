# Day 3: Lobby

## Problem

Each line of the input represents a **battery bank** — a string of digits. The goal is to extract a voltage value from each bank and sum them all up.

A voltage value is formed by reading digits from the bank in a specific order based on selecting the **largest digit** found within a sliding search window.

### Part 1 — Two-digit voltage

For each bank, extract a **two-digit voltage**:

1. Find the largest digit in the entire bank. Call it the **tens digit**.
2. If that largest digit is the **last character**, look to its left for the second largest; otherwise look to its **right** for the second largest.
3. Combine them as `tens_digit * 10 + ones_digit`.

Sum the voltages across all banks.

**Solution:** `first_part.py` finds the biggest element and its index, then determines the search area for the second digit based on whether the biggest is at the end or not.

### Part 2 — Twelve-digit voltage

For each bank, extract a **twelve-digit voltage**:

1. Starting from the full bank, repeatedly find the largest digit within the window `bank[0 : current_position + 1]`, where the window shrinks by one from the right each iteration (12 rounds total).
2. After selecting a digit at index `i`, the next search starts from `i + 1` onwards.
3. Each selected digit becomes the next digit of the voltage number (most significant first).

Sum the twelve-digit voltages across all banks.

**Solution:** `second_part.py` uses a loop of 12 iterations, each time narrowing the search window and advancing the start position past the chosen digit, accumulating the result as `voltage = voltage * 10 + biggest`.
