dungeon_rooms = input().split('|')
health = 100
bitcoins = 0
count_room = 0
hero_is_not_die = True
for current_room in dungeon_rooms:
    count_room += 1
    room = current_room.split()
    command = room[0]
    number = int(room[1])
    if command == 'potion':
        current_state = health
        health += number
        if health > 100:
            health = 100
        amount = health - current_state
        print(f'You healed for {amount} hp.')
        print(f'Current health: {health} hp.')
    elif command == 'chest':
        bitcoins += number
        print(f'You found {number} bitcoins.')
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {count_room}')
            hero_is_not_die = False
            break
if hero_is_not_die:
    print("You've made it!")
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')
