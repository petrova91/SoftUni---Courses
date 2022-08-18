def validation_password(user_password):
    upper_char = 0
    lower_char = 0
    digits = 0
    other_symbols = 0
    for char in user_password:
        if char.isdigit():
            digits += 1
        elif char.isupper():
            upper_char += 1
        elif char.islower():
            lower_char += 1
        elif char != "_":
            other_symbols += 1
    if len(user_password) < 8:
        print("Password must be at least 8 characters long!")
    if other_symbols > 0:
        print("Password must consist only of letters, digits and _!")
    if upper_char == 0:
        print("Password must consist at least one uppercase letter!")
    if lower_char == 0:
        print("Password must consist at least one lowercase letter!")
    if digits == 0:
        print("Password must consist at least one digit!")


password = input()
command = input()
while not command == "Complete":
    data = command.split()
    name_command = data[0]
    if name_command == "Make":
        second_name = data[1]
        index = int(data[2])
        if second_name == "Upper":
            password = password[:index] + password[index].upper() + password[index + 1:]
        elif second_name == "Lower":
            password = password[:index] + password[index].lower() + password[index + 1:]
        print(password)
    elif name_command == "Insert":
        index = int(data[1])
        char = data[2]
        if 0 <= index < len(password):
            password = password[:index] + char + password[index:]
            print(password)
    elif name_command == "Replace":
        char = data[1]
        value = int(data[2])
        if char in password:
            new_char = ord(char) + value
            password = password.replace(char, chr(new_char))
            print(password)
    elif name_command == "Validation":
        validation_password(password)
    command = input()
