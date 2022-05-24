end_first_number = int(input())
end_second_number = int(input())
end_third_number = int(input())
for current_first_number in range(2, end_first_number + 1, 2):
    for current_second_number in range(2, end_second_number + 1):
        if current_second_number == 2 or current_second_number == 3 or current_second_number == 5 or current_second_number == 7:
            for current_third_number in range(2, end_third_number + 1, 2):
                print(f'{current_first_number} {current_second_number} {current_third_number}')
