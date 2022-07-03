number_of_lines = int(input())
positive_numbers = list()
negative_numbers = list()
positive_counter = 0
sum_of_negatives = 0
for i in range(number_of_lines):
    number = int(input())
    if number >= 0:
        positive_counter += 1
        positive_numbers.append(number)
    else:
        sum_of_negatives += number
        negative_numbers.append(number)
print(positive_numbers)
print(negative_numbers)
print(f'Count of positives: {positive_counter}')
print(f'Sum of negatives: {sum_of_negatives}')