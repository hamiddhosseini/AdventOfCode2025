from typing import Tuple

def load_battery_banks(file_name: str) -> list[str]:
    battery_banks = []
    with open(file_name) as f:
        battery_banks = f.read().splitlines()
    return battery_banks

def calculate_total_voltage(battery_banks: list[str]) -> int:
    total_voltage = 0
    for bank in battery_banks:
        voltage = 0
        biggest, biggest_index = find_biggest_element(bank)
        if biggest_index == len(bank) - 1:
            voltage += biggest
            bank = bank[:biggest_index]
            second_biggest, _ = find_biggest_element(bank)
            voltage += second_biggest * 10
        else:
            bank = bank[biggest_index + 1:]
            second_biggest, _ = find_biggest_element(bank)
            voltage += biggest * 10 + second_biggest
        total_voltage += voltage
    return total_voltage

def find_biggest_element(input: str) -> Tuple[int, int]:
    biggest = int(input[0])
    biggest_index = 0
    for element, index in zip(input, range(len(input))):
        if int(element) > biggest:
            biggest = int(element)
            biggest_index = index
    return biggest, biggest_index


battery_banks = load_battery_banks('input_final.txt')
total_voltage = calculate_total_voltage(battery_banks)

print(total_voltage)