count_number = int(input())
sum_even = 0
sum_odd = 0
for count_spin in range(0, count_number):
    number = int(input())
    if count_spin % 2 == 0:
        sum_even += number
    else:
        sum_odd += number
if sum_even == sum_odd:
    print('Yes')
    print(f'Sum = {sum_odd}')
elif sum_even != sum_odd:
    difference = abs(sum_even - sum_odd)
    print('No')
    print(f'Diff = {difference}')
