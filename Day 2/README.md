# Day 2: Gift Shop

The input contains several numeric ranges written as `start-end`, separated by commas. For each range, the program checks every number and adds the invalid IDs to a running total.

Part 1 marks a number as invalid only when it is made of two identical halves. That means the number must have an even number of digits, and the first half must exactly match the second half. Examples include `1212` and `9999`.

The first solution reads all ranges from the input file, iterates through every number in each range, skips numbers with an odd digit count, then compares the two halves of the number as strings. If both halves match, that number is added to the final sum.

Part 2 expands the rule: a number is invalid if the entire value is built by repeating a smaller digit pattern two or more times. Examples include `1212`, `123123`, `121212`, and `111111`.

The second solution still iterates through every number in every range, but it uses a regular expression to detect whether the full number is composed of one repeated substring. When the pattern matches, the number is added to the total.
