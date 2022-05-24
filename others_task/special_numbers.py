number_n = int(input())
for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        for third_digit in range(1, 10):
            for fourth_digit in range(1, 10):
                if number_n % first_digit == 0 and number_n % second_digit == 0 and \
                    number_n % third_digit == 0 and number_n % fourth_digit == 0:
                    print(f'{first_digit}{second_digit}{third_digit}{fourth_digit}', end=' ')