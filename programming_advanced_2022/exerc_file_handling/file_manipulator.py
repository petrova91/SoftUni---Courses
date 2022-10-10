import os

command = input()
while not command == "End":
    data = command.split("-")
    name_data = data[0]
    file_name = data[1]
    if name_data == "Create":
        with open(f"./{file_name}", "w") as file:
            file.write("")
    elif name_data == "Add":
        content = data[2]
        with open(f"./{file_name}", "a") as file:
            file.write(content + "\n")
    elif name_data == "Replace":
        old_string = data[2]
        new_string = data[3]
        try:
            with open(f"./{file_name}", "r+") as file:
                text = file.read()
                text = text.replace(old_string, new_string)
                file.seek(0)
                file.truncate()
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")
    elif name_data == "Delete":
        try:
            os.remove(f"./{file_name}")
        except FileNotFoundError:
            print("An error occurred")
    command = input()