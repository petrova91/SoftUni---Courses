def reversed_indexes(digits, line_command):
    first_index = int(line_command[1])
    second_index = int(line_command[2])
    digits[first_index], digits[second_index] = digits[second_index], digits[first_index]
    return digits


def multiply_element(digits, line_command):
    first_index = int(line_command[1])
    second_index = int(line_command[2])
    result = digits[first_index] * digits[second_index]
    digits[first_index] = result
    return digits


def reduce_num(digits):
    new_numbers = []
    for element in digits:
        result = element - 1
        new_numbers.append(result)
    digits = new_numbers
    return digits


sequence_of_numbers = input().split()
numbers = [int(digit) for digit in sequence_of_numbers]
command = input().split()
while 'end' not in command:
    command_name = command[0]
    if command_name == 'swap':
        numbers = reversed_indexes(numbers, command)
    elif command_name == 'multiply':
        numbers = multiply_element(numbers, command)
    elif command_name == 'decrease':
        numbers = reduce_num(numbers)
    command = input().split()
print(', '.join(map(str, numbers)))