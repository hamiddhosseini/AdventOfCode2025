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

        if direction == 'L':
            current_point -= distance
        elif direction == 'R':
            current_point += distance
        else:
            raise ValueError(f"Invalid direction: {direction}")

        current_point = (current_point - min_pointer) % range_size + min_pointer

        if current_point == count_point:
            counter += 1

    return counter

inputs = extract_inputs('input_final.txt')

result = count_passing_times(
    inputs,
    start_point=50,
    count_point=0,
    min_pointer=0,
    max_pointer=100,
)

print(result)