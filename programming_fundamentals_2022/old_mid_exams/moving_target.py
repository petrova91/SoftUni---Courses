def shoot_command(command_line, num):
    index = int(command_line[1])
    power = int(command_line[2])
    if 0 <= index < len(num):
        num[index] -= power
        if num[index] <= 0:
            num.pop(index)
    return num


def add_command(command_line, num):
    index = int(command_line[1])
    value = int(command_line[2])
    if 0 <= index < len(num):
        num.insert(index, value)
    else:
        print('Invalid placement!')
    return num

def strike_command(command_line, num):
    index = int(command_line[1])
    radius = int(command_line[2])
    start_index = index - radius
    end_index = index + radius
    if 0 <= start_index and end_index < len(num):
        left_part = num[:start_index]
        right_part = num[end_index+1:]
        num = left_part + right_part
    else:
        print('Strike missed!')
    return num


sequence_of_numbers = input().split()
command = input().split()
targets = [int(digit) for digit in sequence_of_numbers]
while command[0] != 'End':
    command_name = command[0]
    if command_name == 'Shoot':
        targets = shoot_command(command, targets)
    elif command_name == 'Add':
        targets = add_command(command, targets)
    elif command_name == 'Strike':
        targets = strike_command(command, targets)
    command = input().split()
targets_as_str = [str(element) for element in targets]
print('|'.join(targets_as_str))