count_floors = int(input())
count_rooms = int(input())
for current_floor in range(count_floors, 0, -1):
    for current_room in range(count_rooms):
        if current_floor == count_floors:
            print(f'L{current_floor}{current_room}', end = ' ')
        elif current_floor % 2 == 0:
            print(f'O{current_floor}{current_room}', end= ' ')
        else:
            print(f'A{current_floor}{current_room}', end = ' ')
    print()
