from collections import deque


def sum_nums(a, b):
    return a + b


def subtract_num(a, b):
    return a - b


def multiply_nums(a, b):
    return a * b


def divide_nums(a, b):
    if not a == 0 and not b == 0:
        return a / b
    return 0


bees = deque(int(num) for num in input().split())
nectar_stack = [int(num) for num in input().split()]
sequence_of_operators = deque(input().split())

total_honey = 0
operator = {
    "+": sum_nums,
    "-": subtract_num,
    "*": multiply_nums,
    "/": divide_nums
}

while nectar_stack:
    if not bees:
        break
    bee = bees[0]
    nectar = nectar_stack.pop()
    if nectar >= bee:
        bee = bees.popleft()
        symbol = sequence_of_operators.popleft()
        total_honey += abs(operator[symbol](bee, nectar))

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar_stack:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_stack)}")

