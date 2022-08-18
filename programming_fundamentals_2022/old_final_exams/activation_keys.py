activation_key = input()
command = input()
while not command == "Generate":
    data = command.split(">>>")
    name_data = data[0]
    if name_data == "Contains":
        substring = data[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif name_data == "Flip":
        case = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        if case == "Upper":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].upper() + activation_key[end_index:]
        elif case == "Lower":
            activation_key = activation_key[:start_index] + activation_key[start_index:end_index].lower() + activation_key[end_index:]
        print(activation_key)
    elif name_data == "Slice":
        start_index = int(data[1])
        end_index = int(data[2])
        activation_key = activation_key[:start_index] + activation_key[end_index:]
        print(activation_key)
    command = input()
print(f"Your activation key is: {activation_key}")