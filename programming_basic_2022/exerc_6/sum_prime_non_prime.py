command = input()
sum_prime_numbers = 0
sum_non_prime_numbers = 0
while command != 'stop':
    number = int(command)
    if number < 0:
        print('Number is negative.')
    else:
        number_is_prime = True
        for current_number in range(2, number - 1):
            if number % current_number == 0:
                number_is_prime = False
                break
        if number_is_prime:
            sum_prime_numbers += number
        else:
            sum_non_prime_numbers += number
    command = input()
print(f'Sum of all prime numbers is: {sum_prime_numbers}')
print(f'Sum of all non prime numbers is: {sum_non_prime_numbers}')
