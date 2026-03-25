
from typing import Tuple, List

def load_battery_banks(file_name: str) -> list[str]:
    battery_banks = []
    with open(file_name) as f:
        battery_banks = f.read().splitlines()
    return battery_banks

def find_biggest_element(input: str) -> Tuple[int, int]:
    biggest = int(input[0])
    biggest_index = 0
    for element, index in zip(input, range(len(input))):
        if int(element) > biggest:
            biggest = int(element)
            biggest_index = index
    return biggest, biggest_index

def calculate_total_voltage(battery_banks: list[str]) -> int:
    total_voltage = 0
    for bank in battery_banks:
        voltage = 0
        remaining_length = 12
        search_area = bank
        while remaining_length > 0:
            biggest, biggest_index = find_biggest_element(search_area[0:(len(search_area) - (remaining_length)) + 1])
            voltage = voltage * 10 + biggest
            remaining_length -= 1
            search_area = search_area[biggest_index + 1:]
        total_voltage += voltage
    return total_voltage

battery_banks = load_battery_banks('input_final.txt')
total_voltage = calculate_total_voltage(battery_banks)

print(total_voltage)