sequence_of_number = input().split()
numbers_as_integer = []
for element in sequence_of_number:
    numbers_as_integer.append(int(element))
is_even = lambda num: num % 2 == 0
even_numbers = list(filter(is_even, numbers_as_integer))
print(even_numbers)
