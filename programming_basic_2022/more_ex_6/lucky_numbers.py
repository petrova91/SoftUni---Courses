number = int(input())
for first_number in range(1, 9 + 1):
    for second_number in range(1, 9 + 1):
        for third_number in range(1, 9 + 1):
            for fourth_number in range(1, 9 + 1):
                first_sum = first_number + second_number
                second_sum = third_number + fourth_number
                if first_sum == second_sum and number % first_sum == 0:
                    happy_number = f'{first_number}{second_number}{third_number}{fourth_number}'
                    print(f'{happy_number}', end=' ')