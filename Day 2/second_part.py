
import re

def load_input_data(file_name: str) -> list[str]:
    with open(file_name, 'r') as file:
        data = file.read()

    input_ranges = data.split(',')
    return input_ranges

input_ranges = load_input_data('input_final.txt')

counter = 0
for input_range in input_ranges:
    start, end = map(int, input_range.split('-'))
    for number in range(start, end + 1):
        len_number = len(str(number))
        reg_pattern = r'^(\d{1,})\1+$'
        if re.match(reg_pattern, str(number)):
            counter += number

print(counter)