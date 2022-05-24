number_n = int(input())
number_m = int(input())
number_s = int(input())
for current_number in range(number_m, number_n-1, -1):
    if current_number % 2 == 0 and current_number % 3 ==0:
        if current_number != number_s:
            print(f'{current_number}', end=' ')
        else:
            break

