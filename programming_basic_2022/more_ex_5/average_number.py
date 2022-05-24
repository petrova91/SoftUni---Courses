number = int(input())
sum = 0
for current_spin in range(number):
    current_number = int(input())
    sum += current_number
average_sum = sum / number
print(f'{average_sum:.2f}')