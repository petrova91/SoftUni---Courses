is_climb = input()
counter_days = 1
start_climb = 5364
end_climb = 8848
height = start_climb
while is_climb != 'END':
    if is_climb == 'Yes':
        counter_days += 1
        more_climb_metres = int(input())
        if counter_days > 5:
            break
        height += more_climb_metres
    else:
        more_climb_metres = int(input())
        height += more_climb_metres
    if height >= end_climb:
        break
    is_climb = input()
if height >= end_climb:
    print(f'Goal reached for {counter_days} days!')
else:
    print('Failed!')
    print(f'{height}')

