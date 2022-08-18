def replace_symbol(text, data_line):
    data = data_line.split()
    current_symbol = data[1]
    new_symbol = data[2]
    text = text.replace(current_symbol, new_symbol)
    print(text)
    return text


def check_indexes(start_index, end_index, text):
    if 0 <= start_index < len(text) and 0 <= end_index < len(text):
        return True
    return False


def cut_command(text, data_line):
    data = data_line.split()
    start_index = int(data[1])
    end_index = int(data[2])
    if check_indexes(start_index, end_index, text):
        text = text[:start_index] + text[end_index+1:]
        print(text)
        return text
    else:
        print("Invalid indices!")


def change_typeface(text, data_line):
    data = data_line.split()
    type_font = data[1]
    if type_font == "Upper":
        text = text.upper()
    elif type_font == "Lower":
        text = text.lower()
    print(text)
    return text


def check_string(text, data_line):
    data = data_line.split()
    string = data[1]
    if string in text:
        print(f"Message contains {string}")
    else:
        print(f"Message doesn't contain {string}")


def sum_symbols(text, data_line):
    data = data_line.split()
    start_index = int(data[1])
    end_index = int(data[2])
    sum_symbols = 0
    if check_indexes(start_index, end_index, text):
        substring = text[start_index:end_index+1]
        for sym in substring:
            sum_symbols += ord(sym)
        print(sum_symbols)
    else:
        print("Invalid indices!")


some_text = input()
command = input()
while not command == "Finish":
    name_data = command.split()[0]
    if name_data == "Replace":
        some_text = replace_symbol(some_text, command)
    elif name_data == "Cut":
        some_text = cut_command(some_text, command)
    elif name_data == "Make":
        some_text = change_typeface(some_text, command)
    elif name_data == "Check":
        check_string(some_text, command)
    elif name_data == "Sum":
        sum_symbols(some_text, command)
    command = input()