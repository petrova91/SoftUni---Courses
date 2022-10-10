from collections import deque


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a // b


def multiply(a, b):
    return a * b


text = input().split()

numbers = deque()
operators = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

for symbol in text:
    if symbol in "+-*/":
        while len(numbers) > 1:
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            result = operators[symbol](first_num, second_num)
            numbers.appendleft(result)
    else:
        numbers.append(int(symbol))
print(numbers.pop())
