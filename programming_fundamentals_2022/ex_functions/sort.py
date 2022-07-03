sequence_of_numbers = input(). split()
numbers_as_integer = []
for element in sequence_of_numbers:
    numbers_as_integer.append(int(element))
sorted_numbers = sorted(numbers_as_integer)
print(sorted_numbers)