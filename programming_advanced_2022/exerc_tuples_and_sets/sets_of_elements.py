def add_digit_to_set(numbers, count_nums):
    for _ in range(count_nums):
        num = int(input())
        numbers.add(num)
    return numbers


len_set_a, len_set_b = input().split()

len_set_a = int(len_set_a)
len_set_b = int(len_set_b)
set_a = set()
set_b = set()

set_a = add_digit_to_set(set_a, len_set_a)
set_b = add_digit_to_set(set_b, len_set_b)

repeated_elem = set_a.intersection(set_b)

for elem in repeated_elem:
    print(elem)