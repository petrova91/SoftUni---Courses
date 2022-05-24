name_player = input()
start_points = 301
game_is_win = False
successful_shots = 0
unsuccessful_shots = 0
field = input()
while field != 'Retire':
    current_points = int(input())
    points = 0
    if field == 'Single':
        points = current_points
    elif field == 'Double':
        points = current_points * 2
    elif field == 'Triple':
        points = current_points * 3
    if points <= start_points:
        start_points -= points
        successful_shots += 1
    else:
        unsuccessful_shots += 1
        field = input()
        continue
    if start_points == 0:
        game_is_win = True
        break
    field = input()
if game_is_win:
    print(f'{name_player} won the leg with {successful_shots} shots.')
else:
    print(f'{name_player} retired after {unsuccessful_shots} unsuccessful shots.')