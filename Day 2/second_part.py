
import re


file_name = 'input2.txt'

with open(file_name, 'r') as file:
    data = file.read()

input_ranges = data.split(',')

counter = 0
for input_range in input_ranges:
    start, end = map(int, input_range.split('-'))
    # print(f"Start: {start}, End: {end}")
    for number in range(start, end + 1):
        len_number = len(str(number))
        # if len_number % 2 != 0:
        #     continue
        # first_half = str(number)[:len(str(number)) // 2]
        # second_half = str(number)[len(str(number)) // 2:]
        # if first_half == second_half:
        #     # print(f"Found number: {number}")
            # counter += number
        reg_pattern = r'^(\d{1,})\1+$'
        if re.match(reg_pattern, str(number)):
            print(f"Found number: {number}")
            counter += number
print(counter)