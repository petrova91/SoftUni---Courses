def found_sum_divisors(digit):
    sum_divisors = 0
    for current_divisor in range(1, digit):
        if digit % current_divisor == 0:
            sum_divisors += current_divisor
    return sum_divisors


number = int(input())
sum_all_divisors = found_sum_divisors(number)
if sum_all_divisors == number:
    print('We have a perfect number!')
else:
    print("It's not so perfect.")