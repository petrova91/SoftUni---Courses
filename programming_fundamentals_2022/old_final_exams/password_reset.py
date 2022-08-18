some_string = input()
command = input()
while not command == "Done":
    data = command.split()
    command_name = data[0]
    if command_name == "TakeOdd":
        message = ""
        for index in range(1, len(some_string), 2):
            message += some_string[index]
        some_string = message
        print(some_string)
    elif command_name == "Cut":
        index = int(data[1])
        length = int(data[2])
        substring = some_string[index:index+length]
        some_string = some_string.replace(substring, "", 1)
        print(some_string)
    elif command_name == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in some_string:
            some_string = some_string.replace(substring, substitute)
            print(some_string)
        else:
            print("Nothing to replace!")
    command = input()
print(f"Your password is: {some_string}")