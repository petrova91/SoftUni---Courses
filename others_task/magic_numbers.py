magic_number = int(input())
for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        for third_digit in range(1, 10):
            for fourth_digit in range(1, 10):
                for fifth_digit in range(1, 10):
                    for sixth_digit in range(1,10):
                        if first_digit * second_digit * third_digit * forth_digit * fifth_digit * sixth_digit == magic_number:
                            print(f'{first_digit}{second_digit}{third_digit}{forth_digit}{fifth_digit}{sixth_digit}', end=' ')