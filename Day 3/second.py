
from typing import Tuple, Dict

file_name = 'input2.txt'

battery_banks = []
with open(file_name) as f:
    battery_banks = f.read().splitlines()

def find_biggest_element(input: str) -> Tuple[int, int]:
    biggest = int(input[0])
    biggest_index = 0
    for element, index in zip(input, range(len(input))):
        if int(element) > biggest:
            biggest = int(element)
            biggest_index = index
    return biggest, biggest_index

total_voltage = 0
for bank in battery_banks:
    voltage = 0
    remaining_length = 12
    search_area = bank
    while remaining_length > 0:
        # print(f"Search are: {search_area} -> 0: {(len(search_area))} - {((remaining_length))}")
        biggest, biggest_index = find_biggest_element(search_area[0:(len(search_area) - (remaining_length)) + 1])
        voltage = voltage * 10 + biggest
        remaining_length -= 1
        search_area = search_area[biggest_index + 1:]
        # print(f"biggest: {biggest}, biggest_index: {biggest_index}, voltage: {voltage}, remaining_length: {remaining_length}, search_area: {search_area}")
    # print(voltage)
    total_voltage += voltage
print(total_voltage)