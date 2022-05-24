start_number = int(input())
end_number = int(input())
for first_number in range(start_number, end_number + 1):
    for second_number in range(start_number, end_number + 1):
        for third_number in range(start_number, end_number + 1):
            for fourth_number in range(start_number, end_number + 1):
                sum = second_number + third_number
                if first_number > fourth_number and sum % 2 == 0 and \
                        ((first_number % 2 == 0 and fourth_number % 2 == 1) or
                        (first_number % 2 == 1 and fourth_number % 2 == 0)):
                    print(f'{first_number}{second_number}{third_number}{fourth_number}', end=' ')