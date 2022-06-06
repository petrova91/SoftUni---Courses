working_day_events = input().split('|')
current_energy = 100
coins = 100
bakery_is_open = True
for element in working_day_events:
    current_event = element.split('-')
    event_name = current_event[0]
    number = int(current_event[1])
    if event_name == 'rest':
        temporary_energy = current_energy
        current_energy += number
        if current_energy > 100:
            current_energy = 100
        gained_energy = current_energy - temporary_energy
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {current_energy}.')
    elif event_name == 'order':
        if current_energy >= 30:
            current_energy -= 30
            coins += number
            print(f'You earned {number} coins.')
        else:
            current_energy += 50
            print('You had to rest!')
    else:
        if number <= coins:
            coins -= number
            print(f'You bought {event_name}.')
        else:
            bakery_is_open = False
            print(f'Closed! Cannot afford {event_name}.')
            break
if bakery_is_open:
    print('Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {current_energy}')