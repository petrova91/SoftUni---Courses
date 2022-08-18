message = input()
command = input()
while not command == "Reveal":
    command_is_wrong = False
    data = command.split(":|:")
    name_data = data[0]
    if name_data == "InsertSpace":
        index = int(data[1])
        message = message[:index] + " " + message[index:]
    elif name_data == "Reverse":
        substring = data[1]
        if substring in message:
            new_substring = substring[::-1]
            message = message.replace(substring, "", 1)
            message += new_substring
        else:
            command_is_wrong = True
            print("error")
    elif name_data == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
    if not command_is_wrong:
        print(message)
    command = input()
print(f"You have a new text message: {message}")
