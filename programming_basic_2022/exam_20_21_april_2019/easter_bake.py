import math

count_easter_bread = int(input())
grams_sugar_in_one_package = 950
grams_flour_in_one_package = 750
max_count_sugar = 0
max_count_flour = 0
total_count_sugar = 0
total_count_flour = 0
for current_easter_bread in range(count_easter_bread):
    count_sugar = int(input())
    count_flour = int(input())
    total_count_sugar += count_sugar
    total_count_flour += count_flour
    if count_sugar > max_count_sugar:
        max_count_sugar = count_sugar
    if count_flour > max_count_flour:
        max_count_flour = count_flour
packages_sugar = total_count_sugar / grams_sugar_in_one_package
packages_flour = total_count_flour / grams_flour_in_one_package
print(f'Sugar: {math.ceil(packages_sugar)}')
print(f'Flour: {math.ceil(packages_flour)}')
print(f'Max used flour is {max_count_flour} grams, max used sugar is {max_count_sugar} grams.')
