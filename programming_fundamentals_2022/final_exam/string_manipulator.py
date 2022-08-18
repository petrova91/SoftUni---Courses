some_string = input()
command = input()
while not command == "End":
    data = command.split()
    name_data = data[0]
    if name_data == "Translate":
        symbol = data[1]
        new_symbol = data[2]
        some_string = some_string.replace(symbol, new_symbol)
        print(some_string)
    elif name_data == "Includes":
        text = data[1]
        if text in some_string:
            print("True")
        else:
            print("False")
    elif name_data == "Start":
        some_text = data[1]
        is_true = some_string.startswith(some_text)
        print(is_true)
    elif name_data == "Lowercase":
        some_string = some_string.lower()
        print(some_string)
    elif name_data == "FindIndex":
        symbol = data[1]
        index = some_string.rindex(symbol)
        print(index)
    elif name_data == "Remove":
        start = int(data[1])
        count = int(data[2])
        end = start + count
        some_string = some_string[:start] + some_string[end:]
        print(some_string)
    command = input()