first_number = int(input())
second_number = int(input())
operation = input()
even_or_odd = 'even'
if operation == '+':
    result = first_number + second_number
    if result % 2 == 0:
        print(f'{first_number} {operation} {second_number} = {result} - {even_or_odd}')
    else:
        even_or_odd = 'odd'
        print(f'{first_number} {operation} {second_number} = {result} - {even_or_odd}')
elif operation == '-':
    result = first_number - second_number
    if result % 2 == 0:
        print(f'{first_number} {operation} {second_number} = {result} - {even_or_odd}')
    else:
        even_or_odd = 'odd'
        print(f'{first_number} {operation} {second_number} = {result} - {even_or_odd}')
elif operation == '*':
    result = first_number * second_number
    if result % 2 == 0:
        print(f'{first_number} {operation} {second_number} = {result} - {even_or_odd}')
    else:
        even_or_odd = 'odd'
        print(f'{first_number} {operation} {second_number} = {result} - {even_or_odd}')
elif operation == '/' and second_number !=0:
    result = first_number / second_number
    print(f'{first_number} / {second_number} = {result:.2f}')
elif operation == '/' and second_number == 0:
    print(f'Cannot divide {first_number} by zero')
elif operation == '%' and second_number != 0:
    result = first_number % second_number
    print(f'{first_number} % {second_number} = {result}')
elif operation == '%' and second_number == 0:
    print(f'Cannot divide {first_number} by zero')