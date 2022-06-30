sequence_of_symbols = input().split()
command = input().split()
count_moves = 0
while 'end' not in command:
    first_index = int(command[0])
    second_index = int(command[1])
    count_moves += 1
    if first_index == second_index or first_index < 0 or first_index >= len(sequence_of_symbols)\
        or second_index < 0 or second_index >= len(sequence_of_symbols):
        middle = len(sequence_of_symbols) // 2
        left_part = sequence_of_symbols[:middle]
        right_part = sequence_of_symbols[middle:]
        add_element = [f"-{count_moves}a"]*2
        sequence_of_symbols = left_part+add_element+right_part
        print('Invalid input! Adding additional elements to the board')
    elif sequence_of_symbols[first_index] == sequence_of_symbols[second_index]:
        element = sequence_of_symbols[first_index]
        print(f'Congrats! You have found matching elements - {sequence_of_symbols[first_index]}!')
        sequence_of_symbols.remove(sequence_of_symbols[first_index])
        change_second_index = sequence_of_symbols.index(element)
        sequence_of_symbols.remove(sequence_of_symbols[change_second_index])
    elif sequence_of_symbols[first_index] != sequence_of_symbols[second_index]:
        print('Try again!')
    if len(sequence_of_symbols) == 0:
        print(f'You have won in {count_moves} turns!')
        break
    command = input().split()
if len(sequence_of_symbols) > 0:
    print('Sorry you lose :(')
    print(' '.join(sequence_of_symbols))