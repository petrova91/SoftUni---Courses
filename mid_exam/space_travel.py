travel_route = input().split('||')
amount_fuel = int(input())
amount_ammunition = int(input())
for command in travel_route:
    command_line = command.split()
    command_name = command_line[0]
    if command_name == 'Travel':
        count_light_years = int(command_line[1])
        if  count_light_years <= amount_fuel:
            amount_fuel -= count_light_years
            print(f'The spaceship travelled {count_light_years} light-years.')
        else:
            print('Mission failed.')
            break
    elif command_name == 'Enemy':
        enemy_ammunition = int(command_line[1])
        if amount_ammunition >= enemy_ammunition:
            amount_ammunition -= enemy_ammunition
            print(f'An enemy with {enemy_ammunition} armour is defeated.')
        else:
            fuel_for_run = 2 * enemy_ammunition
            if fuel_for_run <= amount_fuel:
                amount_fuel -= fuel_for_run
                print(f'An enemy with {enemy_ammunition} armour is outmaneuvered.')
            else:
                print('Mission failed.')
                break
    elif command_name == 'Repair':
        bonus = int(command_line[1])
        count_add_fuel = bonus
        count_add_ammunition = bonus * 2
        amount_fuel += count_add_fuel
        amount_ammunition += count_add_ammunition
        print(f'Ammunitions added: {count_add_ammunition}.')
        print(f'Fuel added: {count_add_fuel}.')
    elif command_name == 'Titan':
        print('You have reached Titan, all passengers are safe.')
        break