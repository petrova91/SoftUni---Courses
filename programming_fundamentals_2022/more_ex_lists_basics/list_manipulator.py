line_numbers = input().split()
line_numbers_as_integer = list(map(int, line_numbers))
command = input().split(' ')
while 'end' not in command:
    if 'end' in command:
        break
    name_command = command[0]
    number = command[1]
    type_number = command[-1]
    odd_numbers = []
    even_numbers = []
    for element in line_numbers_as_integer:
        if element % 2 == 0:
            even_numbers.append(element)
        else:
            odd_numbers.append(element)
    if name_command == 'exchange':
        number = int(number)
        if 0 > number or number >= len(line_numbers):
            print('Invalid index')
        else:
            left_part = line_numbers_as_integer[number + 1:]
            right_part = line_numbers_as_integer[:number + 1]
            line_numbers_as_integer = left_part + right_part
    elif name_command == 'max' or name_command == 'min':
        if name_command == 'max' and type_number == 'even':
            if len(even_numbers) == 0:
                print('No matches')
            else:
                for index in range(len(line_numbers_as_integer) - 1, -1, -1):
                    if line_numbers_as_integer[index] == max(even_numbers):
                        print(index)
                        break
        elif name_command == 'max' and type_number == 'odd':
            if len(odd_numbers) == 0:
                print('No matches')
            else:
                for index in range(len(line_numbers_as_integer) - 1, -1, -1):
                    if line_numbers_as_integer[index] == max(odd_numbers):
                        print(index)
                        break
        elif name_command == 'min' and type_number == 'even':
            if len(even_numbers) == 0:
                print('No matches')
            else:
                for index in range(len(line_numbers_as_integer) - 1, -1, -1):
                    if line_numbers_as_integer[index] == min(even_numbers):
                        print(index)
                        break
        if name_command == 'min' and type_number == 'odd':
            if len(even_numbers) == 0:
                print('No matches')
            else:
                for index in range(len(line_numbers_as_integer) - 1, -1, -1):
                    if line_numbers_as_integer[index] == min(odd_numbers):
                        print(index)
                        break
    elif name_command == 'first' or name_command == 'last':
        list_element = []
        number = int(number)
        if number > len(line_numbers_as_integer):
            print('Invalid count')
        elif name_command == 'first' and type_number == 'even':
            list_element = even_numbers[:number]
            print(list_element)
        elif name_command == 'first' and type_number == 'odd':
            list_element = odd_numbers[:number]
            print(list_element)
        elif name_command == 'last' and type_number == 'even':
            list_element = even_numbers[-number:]
            print(list_element)
        elif name_command == 'last' and type_number == 'odd':
            list_element = odd_numbers[-number:]
            print(list_element)
    command = input().split(' ')
print(line_numbers_as_integer)
