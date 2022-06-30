count_rooms = int(input())
count_free_chairs = 0
chairs_is_enough = True
for current_room in range(1, count_rooms+1):
    information = input().split()
    chairs_in_room = information[0]
    count_visitors = int(information[1])
    if count_visitors > len(chairs_in_room):
        needed_chairs_in_room = count_visitors - len(chairs_in_room)
        print(f'{needed_chairs_in_room} more chairs needed in room {current_room}')
        chairs_is_enough = False
    else:
        count_free_chairs += len(chairs_in_room) - count_visitors
if chairs_is_enough:
    print(f'Game On, {count_free_chairs} free chairs left')