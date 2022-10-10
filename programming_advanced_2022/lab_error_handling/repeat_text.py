text = input()

try:
    type_to_repeat = int(input())
    print(text * type_to_repeat)
except ValueError:
    print("Variable times must be an integer")