numbers = input()
list_number = numbers.split(' ')
invert_digits = []
for digit in list_number:
    invert_value = int(digit) * (-1)
    invert_digits.append(invert_value)
print(invert_digits)