start_first_numbers = int(input())
start_second_numbers = int(input())
different_first_numbers = int(input())
different_second_numbers = int(input())
end_first_numbers = start_first_numbers + different_first_numbers
end_second_numbers = start_second_numbers + different_second_numbers
for first_numbers in range(start_first_numbers, end_first_numbers+1):
    prime_count = 0
    for first_digit in range(2, first_numbers):
        if first_numbers % first_digit == 0:
            prime_count += 1
    if prime_count == 0:
        for second_numbers in range(start_second_numbers, end_second_numbers+1):
            prime_count = 0
            for second_digit in range(2, second_numbers):
                if second_numbers % second_digit == 0:
                    prime_count += 1
            if prime_count == 0:
                print(f'{first_numbers}{second_numbers}')

# друго решение:
first_pair = int(input())
second_pair = int(input())
first_pair_plus = int(input())
second_pair_plus = int(input())

for a in range(first_pair, (first_pair + first_pair_plus) + 1):
    for b in range(second_pair, (second_pair + second_pair_plus) + 1):
        is_a_prime = True
        is_b_prime = True
        for i in range(2, a):
            if a % i == 0:
                is_a_prime = False
                break
        for j in range(2, b):
            if b % j == 0:
                is_b_prime = False
                break
        if is_a_prime and is_b_prime:
            print(f"{a}{b}")



