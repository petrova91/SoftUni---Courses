start_number = input()
end_number = input()
for first_digit in range(int(start_number[0]), int(end_number[0]) + 1):
    for second_digit in range(int(start_number[1]), int(end_number[1]) + 1):
        for third_digit in range(int(start_number[2]), int(end_number[2]) + 1):
            for fourth_digit in range(int(start_number[3]), int(end_number[3]) + 1):
                if first_digit % 2 == 1 and second_digit % 2 == 1 and \
                        third_digit % 2 == 1 and fourth_digit % 2 == 1:
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')

