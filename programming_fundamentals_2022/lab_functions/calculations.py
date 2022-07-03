def calculation(num_a, num_b, operation):
    result = None
    if operation == 'multiply':
        result = num_a * num_b
    elif operation == 'divide':
        result = int(num_a / num_b)
    elif operation == 'add':
        result = num_a + num_b
    elif operation == 'subtract':
        result = num_a - num_b
    return result


operator_as_string = input()
first_number = int(input())
second_number = int(input())
print(calculation(first_number, second_number, operator_as_string))