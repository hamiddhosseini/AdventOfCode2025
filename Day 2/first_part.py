
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
        if len_number % 2 != 0:
            continue
        first_half = str(number)[:len(str(number)) // 2]
        second_half = str(number)[len(str(number)) // 2:]
        if first_half == second_half:
            counter += number

print(counter)