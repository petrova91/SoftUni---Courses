first_number = int(input())
second_number = int(input())
value_a = first_number
value_b = second_number
print('Before:')
print(f'a = {value_a}')
print(f'b = {value_b}')
value_a = second_number
value_b = first_number
print('After:')
print(f'a = {value_a}')
print(f'b = {value_b}')
