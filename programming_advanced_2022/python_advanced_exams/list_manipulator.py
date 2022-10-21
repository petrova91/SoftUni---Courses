def list_manipulator(numbers, first_command, second_command, *args):
    if first_command == "add" and second_command == "beginning":
        return list(args) + numbers
    elif first_command == "add" and second_command == "end":
        return numbers + list(args)
    elif first_command == "remove" and second_command == "beginning":
        if args:
            count_num = args[0]
            return numbers[count_num:]
        else:
            return numbers[1:]
    elif first_command == "remove" and second_command == "end":
        if args:
            count_num = args[0]
            return numbers[:len(numbers) - count_num]
        else:
            return numbers[:len(numbers) - 1]


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
