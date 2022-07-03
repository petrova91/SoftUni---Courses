number = input()
list_number = []
max_number = ''
for index, digit in enumerate(number):
    list_number.append(digit)
list_number.sort()
list_number = list(reversed(list_number))
for digit in list_number:
    max_number += digit
print(max_number)
