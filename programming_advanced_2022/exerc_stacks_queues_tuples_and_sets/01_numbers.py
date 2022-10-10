first_nums = set(int(num) for num in input().split())
second_nums = set(int(digit) for digit in input().split())
count_lines = int(input())

for _ in range(count_lines):
    name_command, type_set, *numbers = input().split()
    numbers = set(int(number) for number in numbers)
    if name_command == "Add":
        if type_set == "First":
            first_nums = first_nums.union(numbers)
        elif type_set == "Second":
            second_nums = second_nums.union(numbers)
    elif name_command == "Remove":
        if type_set == "First":
            first_nums = first_nums.difference(numbers)
        elif type_set == "Second":
            second_nums = second_nums.difference(numbers)
    elif name_command == "Check":
        print(first_nums.issubset(second_nums) or second_nums.issubset(first_nums))

print(*sorted(first_nums), sep=", ")
print(*sorted(second_nums), sep=", ")