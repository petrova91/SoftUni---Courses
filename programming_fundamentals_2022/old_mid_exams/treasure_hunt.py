initial_loot = input().split('|')
command = input().split()
stolen_items = []
while command != 'Yohoho!':
    command_name = command[0]
    if command_name == 'Yohoho!':
        break
    elif command_name == 'Loot':
        items = command[1:]
        for element in items:
            if element not in initial_loot:
                initial_loot.insert(0, element)
    elif command_name == 'Drop':
        index = int(command[1])
        if index < len(initial_loot):
            remove_item = initial_loot.pop(index)
            initial_loot.append(remove_item)
    elif command_name == 'Steal':
        count_stolen_items = int(command[1])
        if count_stolen_items >= len(initial_loot):
            stolen_items = initial_loot.copy()
            initial_loot.clear()
        else:
            stolen_items = initial_loot[-count_stolen_items:]
            initial_loot = initial_loot[:(len(initial_loot)- count_stolen_items)]
        print(', '.join(stolen_items))
    command = input().split()
if len(initial_loot) == 0:
    print('Failed treasure hunt.')
else:
    sum_all_length_items = 0
    for item in initial_loot:
        sum_all_length_items += len(item)
    average_gain = sum_all_length_items / len(initial_loot)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')
