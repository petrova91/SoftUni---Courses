start_number = int(input())
end_number = int(input())
magic_number = int(input())
counter = 0
is_find = False
for first_number in range(start_number, end_number + 1):
    for second_number in range(start_number, end_number + 1):
        sum = first_number + second_number
        counter += 1
        if sum == magic_number:
            is_find = True
            break
    if is_find:
        break
if is_find:
    print(f'Combination N:{counter} ({first_number} + {second_number} = {sum})')
else:
    print(f'{counter} combinations - neither equals {magic_number}')
