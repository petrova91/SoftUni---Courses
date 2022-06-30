def sum_numbers(num_a, num_b):
    return num_a + num_b


def subtract(sum_num, num_c):
    return sum_num - num_c


def add_and_subtract(num_a, num_b, num_c):
    sum_numbers(num_a, num_b)
    subtract(sum_numbers(num_a, num_b), num_c)
    print(subtract(sum_numbers(num_a, num_b), num_c))


first_number = int(input())
second_number = int(input())
third_number = int(input())
add_and_subtract(first_number, second_number, third_number)
