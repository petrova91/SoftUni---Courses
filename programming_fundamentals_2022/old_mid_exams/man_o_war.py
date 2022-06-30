def calculate_health_status(current_command, ship):
    command_name = current_command[0]
    index = int(current_command[1])
    points = int(current_command[-1])
    if command_name == 'Fire':
        if 0 <= index < len(ship):
            ship[index] -= points
    elif command_name == 'Defend':
        end_index = int(current_command[2])
        if 0 <= index < end_index and index < end_index < len(ship):
            for i in range(index, end_index+1):
                ship[i] -= points
                if ship[i] <= 0:
                    break
    elif command_name == 'Repair':
        if 0 <= index < len(ship):
            ship[index] += points
            if ship[index] > max_health_capacity:
                ship[index] = max_health_capacity
    return ship


status_pirate_ship = input().split('>')
status_warship = input().split('>')
max_health_capacity = int(input())
# sections_as_integer
pirate_ship = list(map(int, status_pirate_ship))
warship = list(map(int, status_warship))
ship_is_sinks = False
command = input().split()
while command != 'Retire':
    if 'Retire' in command:
        break
    elif 'Fire' in command:
        calculate_health_status(command, warship)
        for element in warship:
            if element <= 0:
                ship_is_sinks = True
                print('You won! The enemy ship has sunken.')
                break
        if ship_is_sinks:
            break
    elif 'Defend' in command:
        calculate_health_status(command, pirate_ship)
        for element in pirate_ship:
            if element <= 0:
                ship_is_sinks = True
                print('You lost! The pirate ship has sunken.')
                break
        if ship_is_sinks:
            break
    elif 'Repair' in command:
        calculate_health_status(command, pirate_ship)
    elif 'Status' in command:
        counter_cell_to_repair = 0
        lower_health_capacity = max_health_capacity * 0.2
        for section in pirate_ship:
            if section < lower_health_capacity:
                counter_cell_to_repair += 1
        print(f'{counter_cell_to_repair} sections need repair.')
    command = input().split()
if ship_is_sinks == False:
    pirate_ship_sum = sum(pirate_ship)
    warship_sum = sum(warship)
    print(f'Pirate ship status: {pirate_ship_sum}')
    print(f'Warship status: {warship_sum}')