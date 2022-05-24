some_string = input()
list_string = some_string.split(', ')
list_string.append('me')
list_string.reverse()
position_wolf = list_string.index('wolf')
position_me = list_string.index('me')
if position_wolf == position_me + 1:
    print('Please go away and stop eating my sheep')
else:
    position_sheep = position_wolf - 1
    print(f'Oi! Sheep number {position_sheep}! You are about to be eaten by a wolf!')