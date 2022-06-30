sequence_of_numbers = input().split()
numbers = [int(digit) for digit in sequence_of_numbers]
average_value = sum(numbers) / len(numbers)
top_numbers = [num for num in numbers if num > average_value]
top_numbers.sort(reverse=True)
if len(top_numbers) > 5:
    top_numbers = top_numbers[:5]
if len(top_numbers) > 0:
    print(' '.join(map(str, top_numbers)))
else:
    print('No')

