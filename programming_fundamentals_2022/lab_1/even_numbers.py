number_n = int(input())
digit_is_even = True
odd_digit = ''
for current_number in range(number_n):
    digit = int(input())
    if digit % 2 != 0:
        digit_is_even = False
        odd_digit = digit
        break
if digit_is_even:
    print('All numbers are even.')
else:
    print(f'{odd_digit} is odd!')

#  друго решение:
#number_n = int(input())
#for current_number in range(number_n):
#    digit = int(input())
#    if digit % 2 != 0:
#        print(f'{digit} is odd!')
#        break
#else:
#    print('All numbers are even.')