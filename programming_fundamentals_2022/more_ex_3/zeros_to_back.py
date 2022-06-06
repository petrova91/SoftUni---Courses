number_as_string = input().split(', ')
zero_counter = 0
while '0' in number_as_string:
    number_as_string.remove('0')
    zero_counter += 1
number_as_integer = list(map(int, number_as_string))
for i in range(zero_counter):
    number_as_integer.append(0)
print(number_as_integer)
