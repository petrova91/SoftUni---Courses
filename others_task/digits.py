number = int(input())
first_digit = number // 100
second_digit = (number // 10) - (first_digit * 10)
third_digit = number % 10
rows_n = first_digit + second_digit
columns_m = first_digit + third_digit
for current_row in range(1, rows_n+1):
    for current_column in range (1, columns_m+1):
        if number % 5 == 0:
            number -= first_digit
        elif number % 3 == 0:
            number -= second_digit
        else:
            number += third_digit
        print(f'{number}', end=' ')
    print()