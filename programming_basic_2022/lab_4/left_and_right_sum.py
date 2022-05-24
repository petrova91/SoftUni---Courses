count_number = int(input())
left_sum = 0
right_sum = 0
for number in range(0, count_number):
    left_number = int(input())
    left_sum += left_number
for number in range(0, count_number):
    right_number = int(input())
    right_sum += right_number
if left_sum == right_sum:
    print(f'Yes, sum = {left_sum}')
elif left_sum != right_sum:
    different = abs(left_sum - right_sum)
    print(f'No, diff = {different}')