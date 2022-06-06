factor = int(input())
count_numbers = int(input())
list_number = []
for digit in range(1, count_numbers+1):
    number = digit * factor
    list_number.append(number)
print(list_number)