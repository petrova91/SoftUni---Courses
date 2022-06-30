def find_result(all_numbers):
    if 0 in all_numbers:
        print('zero')
    else:
        count_negative_num = 0
        for digit in all_numbers:
            if digit < 0:
                count_negative_num += 1
        if count_negative_num == 2 or count_negative_num == 0:
            print('positive')
        else:
            print('negative')


first_number = int(input())
second_number = int(input())
third_number = int(input())
list_numbers = [first_number, second_number, third_number]
find_result(list_numbers)