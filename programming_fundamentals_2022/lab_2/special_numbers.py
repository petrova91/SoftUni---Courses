number_n = int(input())
for current_digit in range(1, number_n+1):
    sum_current_digit = 0
    digit = current_digit
    while digit > 0:
        sum_current_digit += digit % 10
        digit = int(digit / 10)
    if sum_current_digit == 5 or sum_current_digit == 7 or sum_current_digit == 11:
        print(f'{current_digit} -> True')
    else:
        print(f'{current_digit} -> False')