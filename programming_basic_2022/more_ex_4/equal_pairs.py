number_combinations = int(input())
max_difference = 0
difference = 0
sum_numbers_previous = 0
counter = 0
for num in range(number_combinations):
    number1 = int(input())
    number2 = int(input())
    sum_numbers = number1 + number2
    if num == 0:
        sum_numbers_previous = sum_numbers
        continue
    difference = abs(sum_numbers - sum_numbers_previous)
    if sum_numbers == sum_numbers_previous:
        continue
    elif difference > max_difference:
        max_difference = difference
        counter += 1
    sum_numbers_previous = sum_numbers
if counter == 0:
    print(f"Yes, value={sum_numbers_previous}")
else:
    print(f"No, maxdiff={max_difference}")



