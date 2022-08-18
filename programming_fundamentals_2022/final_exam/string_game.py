def change_symbol(string, data):
    name_data, symbol, replacement = data.split()
    string = string.replace(symbol, replacement)
    print(string)
    return string


def check_for_substring(string, data):
    name_data, substring = data.split()
    if substring in string:
        print("True")
    else:
        print("False")


def check_ends(string, data):
    name_data, substring = data.split()
    is_true = string.endswith(substring)
    print(is_true)


def change_font(string):
    string = string.upper()
    print(string)
    return string


def find_index(string, data):
    name_data, symbol = data.split()
    index = string.find(symbol)
    print(index)


def cut_string(string, data):
    name_data, start_index, count_indexes = data.split()
    start = int(start_index)
    end = start + int(count_indexes)
    string = string[start:end]
    print(string)
    return string


text = input()
command = input()
while not command == "Done":
    name_command = command.split()[0]
    if name_command == "Change":
        text = change_symbol(text, command)
    elif name_command == "Includes":
        check_for_substring(text, command)
    elif name_command == "End":
        check_ends(text, command)
    elif name_command == "Uppercase":
        text = change_font(text)
    elif name_command == "FindIndex":
        find_index(text, command)
    elif name_command == "Cut":
        text = cut_string(text, command)
    command = input()