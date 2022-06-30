def modify_list(num,old_index_value):
    new_digits = []
    for element in num:
        if element > old_index_value and element != -1:
            element -= old_index_value
        elif element <= old_index_value and element != -1:
            element += old_index_value
        new_digits.append(element)
    return new_digits


sequence_of_integers = input().split()
count_shots = 0
command = input()
targets = [int(digit) for digit in sequence_of_integers]
while command != 'End':
    index = int(command)
    if 0 <= index < len(targets) and targets[index] != -1:
        value_of_target = targets[index]
        targets[index] = -1
        count_shots += 1
        targets = modify_list(targets, value_of_target)
    command = input()
shoot_target = ' '.join(map(str, targets))
print(f'Shot targets: {count_shots} -> {shoot_target}')