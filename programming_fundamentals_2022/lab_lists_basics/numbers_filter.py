number_of_lines = int(input())
list_digits = []
filtered_list = []
for i in range(number_of_lines):
    digit = int(input())
    list_digits.append(digit)
command = input()
if command == 'even':
    for number in list_digits:
        if number % 2 == 0:
            filtered_list.append(number)
elif command == 'odd':
    for number in list_digits:
        if number % 2 == 1:
            filtered_list.append(number)
elif command == 'negative':
    for number in list_digits:
        if number < 0:
            filtered_list.append(number)
elif command == 'positive':
    for number in list_digits:
        if number >= 0:
            filtered_list.append(number)
print(filtered_list)