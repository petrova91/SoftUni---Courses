def register_command(data, parking):
    user_name = data[1]
    license_plate_number = data[2]
    if user_name in parking:
        print(f'ERROR: already registered with plate number {license_plate_number}')
    else:
        parking[user_name] = license_plate_number
        print(f'{user_name} registered {license_plate_number} successfully')
    return parking


def unregister_command(data, parking):
    user_name = data[1]
    if user_name not in parking:
        print(f'ERROR: user {user_name} not found')
    else:
        parking.pop(user_name)
        print(f'{user_name} unregistered successfully')
    return parking


count_commands = int(input())
parking_dict = {}
for current_command in range(count_commands):
    command = input().split()
    command_name = command[0]
    if command_name == 'register':
        parking_dict = register_command(command, parking_dict)
    elif command_name == 'unregister':
        parking_dict = unregister_command(command, parking_dict)
for user_name, number in parking_dict.items():
    print(f'{user_name} => {number}')