# Day 1: Secret Entrance

The problem describes a scenario where we have a series of movements (left and right) along a number line, starting from a specific point. We need to count how many times we pass a certain point (the "count_point") during these movements. The movements can wrap around within a defined range (from min_pointer to max_pointer).
Once the wrapping is handled correctly, we can simply check if the current point after each movement is equal to the count_point or if we have passed it during the movement.

For the first part, we only need to check if we land on the count_point after each movement. For the second part, we also need to check if we pass the count_point during the movement, which requires us to consider the direction of movement and the wrapping around the range. The test cases provided in the second part help ensure that the logic for counting crossings is correct, including edge cases where we start at a non-zero point and move to zero, or when we move left past zero. These cases were mostly developed to help with the debugging the provided solution and might not be comprehensive for all edge cases, but they do cover some important scenarios.
