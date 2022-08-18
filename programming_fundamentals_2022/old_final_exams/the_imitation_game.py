message = input()
instructions = input()
while not instructions == "Decode":
    data = instructions.split("|")
    name_data = data[0]
    if name_data == "Move":
        count_letters = int(data[1])
        message = message[count_letters:] + message[:count_letters]
    elif name_data == "Insert":
        index = int(data[1])
        value = data[2]
        message = message[:index] + value + message[index:]
    elif name_data == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
    instructions = input()
print(f"The decrypted message is: {message}")