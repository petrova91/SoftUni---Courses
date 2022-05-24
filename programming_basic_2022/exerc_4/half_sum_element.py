import sys

count_number = int(input())
sum_number = 0
max_number = -sys.maxsize
for count_spin in range(count_number):
    number = int(input())
    if number > max_number:
        max_number = number
    sum_number += number
if max_number == sum_number - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    different = abs(max_number - (sum_number - max_number))
    print('No')
    print(f'Diff = {different}')