number = int(input())
first_number = 0
second_number = 0
third_number = 0
sum = 1
count = 1
list_numbers = []
while count <= number:
    print(f'{sum}', end=' ')
    count += 1
    first_number = second_number
    second_number = third_number
    third_number = sum
    sum = first_number + second_number + third_number
