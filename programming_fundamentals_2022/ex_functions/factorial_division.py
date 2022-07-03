def find_factorial(digit):
    digit_factorial = digit
    for number in range(1, digit):
        digit_factorial *= number
    return digit_factorial


first_number = int(input())
second_number = int(input())
first_num_factorial = find_factorial(first_number)
second_num_factorial = find_factorial(second_number)
result = first_num_factorial / second_num_factorial
print(f'{result:.2f}')