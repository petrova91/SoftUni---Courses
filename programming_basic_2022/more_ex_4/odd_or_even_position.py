import sys

range_number = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = - sys.maxsize
even_sum = 0
even_max = - sys.maxsize
even_min = sys.maxsize
for current_number in range(1, range_number + 1):
    number = float(input())
    if current_number % 2 == 1:
        odd_sum += number
        if number < odd_min:
            odd_min = number
        if number > odd_max:
            odd_max = number
    elif current_number % 2 == 0:
        even_sum += number
        if number < even_min:
            even_min = number
        if number > even_max:
            even_max = number
print(f'OddSum={odd_sum:.2f},')
if odd_sum == 0:
    print('OddMin='+'No'+',')
else:
    print(f'OddMin={odd_min:.2f},')
if odd_sum == 0:
    print('OddMax='+'No'+',')
else:
    print(f'OddMax={odd_max:.2f},')
print(f'EvenSum={even_sum:.2f},')
if even_sum == 0:
    print('EvenMin='+'No'+',')
else:
    print(f'EvenMin={even_min:.2f},')
if even_sum == 0:
    print('EvenMax='+'No')
else:
    print(f'EvenMax={even_max:.2f}')
