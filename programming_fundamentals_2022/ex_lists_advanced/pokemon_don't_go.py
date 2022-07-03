def change_num_list(numbers, value):
    new_digits = []
    for digit in numbers:
        if digit <= value:
            digit += value
        else:
            digit -= value
        new_digits.append(digit)
    numbers = new_digits
    return numbers


sequence_of_numbers = input().split()
num = [int(digit) for digit in sequence_of_numbers]
remove_element = []
while len(num) > 0:
    index = int(input())
    element = ''
    if 0 <= index < len(num):
        element = num.pop(index)
    elif index < 0:
        element = num[0]
        num[0] = num[-1]
    elif index >= len(num):
        element = num[-1]
        num[-1] = num[0]
    remove_element.append(element)
    num = change_num_list(num, element)
print(sum(remove_element))