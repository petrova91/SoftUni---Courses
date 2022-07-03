sequence_of_numbers = input().split()
numbers_as_integer = []
for element in sequence_of_numbers:
    numbers_as_integer.append(int(element))
max_number = max(numbers_as_integer)
min_number = min(numbers_as_integer)
sum_of_numbers = sum(numbers_as_integer)
print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {sum_of_numbers}')