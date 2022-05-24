start_number = int(input())
end_number = int(input())
magic_number = int(input())
counter_combination = 0
magic_number_in_found = False
for first_number in range(start_number, end_number+1):
    for second_number in range(start_number, end_number+1):
        counter_combination += 1
        if first_number + second_number == magic_number:
            magic_number_in_found = True
            print(f'Combination N:{counter_combination} ({first_number} + {second_number} = {magic_number})')
            break
    if magic_number_in_found:
        break
if magic_number_in_found == False:
    print(f'{counter_combination} combinations - neither equals {magic_number}')