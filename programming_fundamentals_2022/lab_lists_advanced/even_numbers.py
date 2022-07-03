sequence_of_numbers = input().split(', ')
numbers = list(map(int, sequence_of_numbers))
index_even_num = []
for index, digit in enumerate(numbers):
    if digit % 2 == 0:
        index_even_num.append(index)
print(index_even_num)

