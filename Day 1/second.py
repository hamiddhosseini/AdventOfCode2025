from typing import List

def extract_inputs(file_name:str) -> List[str]:
    with open(file_name) as f:
        lines = f.readlines()

    inputs = []
    for line in lines:
        inputs.append(line.strip().upper())
    return inputs

def count_passing_times(
    inputs: List[str],
    start_point: int,
    count_point: int,
    min_pointer: int,
    max_pointer: int,
) -> int:
    current_point = start_point
    counter = 0
    range_size = max_pointer - min_pointer

    for command in inputs:
        direction = command[0]
        distance = int(command[1:])
        starting_point = current_point

        if direction == 'L':
            current_point -= distance
            if current_point < min_pointer:
                old_counter = counter
                if distance >= range_size:
                    counter += distance // range_size
                    if starting_point - (distance % range_size) < min_pointer and starting_point != count_point:
                        counter += 1
                elif starting_point != count_point:
                    counter += 1
                print(f"Passed {count_point} while moving left from {starting_point} to {current_point} counter change {counter - old_counter} counter={counter}")
        elif direction == 'R':
            current_point += distance
            if current_point > max_pointer:
                old_counter = counter
                if distance >= range_size:
                    counter += distance // range_size
                    if (starting_point + (distance % range_size)) > max_pointer and starting_point != count_point:
                        counter += 1
                elif starting_point != count_point:
                    counter += 1
                print(f"Passed {count_point} while moving right from {starting_point} to {current_point} counter change {counter - old_counter} counter={counter}")
        else:
            raise ValueError(f"Invalid direction: {direction}")

        current_point = (current_point - min_pointer) % range_size + min_pointer
        if current_point == count_point:
            counter += 1
            print(f"Landed on {count_point} counter={counter}")

    return counter

def count_passing_times_v2(
    inputs: List[str],
    start_position: int,
    target_position: int,
    min_range: int,
    max_range: int,
) -> int:
    current_position = start_position
    counter = 0
    range_size = max_range - min_range

    for command in inputs:
        direction = command[0]
        distance = int(command[1:])

        if direction == 'L':
            new_position = current_position - distance
            crossings = (current_position - target_position) // range_size - (new_position - target_position) // range_size
        elif direction == 'R':
            new_position = current_position + distance
            crossings = (new_position - target_position) // range_size - (current_position - target_position) // range_size
        else:
            raise ValueError(f"Invalid direction: {direction}")

        if current_position == target_position:
            crossings -= 1
        counter += max(crossings, 0)

        current_position = (new_position - min_range) % range_size + min_range
        # if current_position == target_position:
        #     counter += 1
    return counter


def solve():
    inputs = extract_inputs("input.txt")

    result = count_passing_times_v2(inputs, 50, 0, 0, 100)

    print(result)

if __name__ == "__main__":
    solve()

# def test_count_passing_times_v2():
assert count_passing_times_v2(["R5", "L3"], 10, 0, 0, 100) == 0, "No crossing should yield zero"
assert count_passing_times_v2(["L10"], 10, 0, 0, 100) == 1, "Start at non-zero and move to zero should count as one crossing"
assert count_passing_times_v2(["L15"], 10, 0, 0, 100) == 1, "Move left past zero should count as one crossing"
assert count_passing_times_v2(["R150"], 50, 0, 0, 100) == 2, "Move right past zero with wrapping should count as two crossings"
assert count_passing_times_v2(["R10"], 0, 0, 0, 100) == 0, "Starting at zero and moving right should not count as crossing"
assert count_passing_times_v2(["L200"], 50, 0, 0, 100) == 2, "Large left jump should count multiple crossings correctly"
assert count_passing_times_v2(["R60", "L120", "R30"], 10, 0, 0, 100) == 1, "Multiple jumps crossing zero should count correctly"
assert count_passing_times_v2(["L10", "R5"], 5, 0, 0, 10) == 2, "Crossing at min_pointer edge should count correctly"
assert count_passing_times_v2(["R380"], 20, 0, 0, 100) == 4, "Multiple full loops should count multiple crossings"
assert count_passing_times_v2(["L150"], 50, 0, 0, 100) == 2, "Large left jump should count multiple crossings correctly"
assert count_passing_times_v2(["R150"], 50, 0, 0, 100) == 2, "Large right jump should count multiple crossings correctly"
assert count_passing_times_v2(["L150", "L50"], 50, 0, 0, 100) == 2, "Two large left jumps should count multiple crossings correctly"
assert count_passing_times_v2(["L150", "R50"], 50, 0, 0, 100) == 2, "Left then right large jumps should count multiple crossings correctly"
assert count_passing_times_v2(["R150", "L50"], 50, 0, 0, 100) == 2, "Right then left large jumps should count multiple crossings correctly"
assert count_passing_times_v2(["R150", "R50"], 50, 0, 0, 100) == 2, "Two large right jumps should count multiple crossings correctly"
assert count_passing_times_v2(["L3"], 2, 0, 0, 100) == 1, "Missed simple left crossing"
assert count_passing_times_v2(["L1"], 1, 0, 0, 100) == 1, "Edge crossing at boundary"
assert count_passing_times_v2(["L2"], 2, 0, 0, 100) == 1, "Landing exactly on zero from left"
assert count_passing_times_v2(["R2"], 99, 0, 0, 100) == 1, "Right crossing near boundary"
assert count_passing_times_v2(["R101"], 0, 0, 0, 100) == 1, "Crossing after starting at zero (should NOT count start)"
assert count_passing_times_v2(["R100"], 0, 0, 0, 100) == 1, "Full loop from zero should count once"
assert count_passing_times_v2(["L2", "R2"], 1, 0, 0, 100) == 2, "Oscillation over zero"
assert count_passing_times_v2(["L100", "R100"], 50, 0, 0, 100) == 2, "Exact landing cycles"
assert count_passing_times_v2(["L51"], 50, 0, 0, 100) == 1, "Cross without multiple wraps"