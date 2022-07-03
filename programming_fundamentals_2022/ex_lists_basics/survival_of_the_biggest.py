list_numbers = input()
count_of_number_to_remove = int(input())
# numbers = []
# biggest_digits = []
# for digit in list_numbers:
#     digit = int(digit)
#     numbers.append(digit)
numbers = list(map(int, list_numbers.split(' ')))
for i in range(count_of_number_to_remove):
    min_digit = min(numbers)
    numbers.remove(min_digit)
# for current_number in numbers:
#     current_number = str(current_number)
#     biggest_digits.append(current_number)
numbers = map(str, numbers)
print(', '.join(numbers))



