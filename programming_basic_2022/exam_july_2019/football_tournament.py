name_football_team = input()
count_competition = int(input())
count_points = 0
count_wins = 0
count_loses = 0
count_draw = 0
for current_competition in range(count_competition):
    result = input()
    if result == 'W':
        points = 3
        count_points += points
        count_wins += 1
    elif result == 'D':
        points = 1
        count_points += points
        count_draw += 1
    elif result == 'L':
        points = 0
        count_points += points
        count_loses += 1
if count_competition == 0:
    print(f"{name_football_team} hasn't played any games during this season.")
else:
    percent_wins = (count_wins / count_competition) * 100
    print(f'{name_football_team} has won {count_points} points during this season.')
    print('Total stats:')
    print(f'## W: {count_wins}')
    print(f'## D: {count_draw}')
    print(f'## L: {count_loses}')
    print(f'Win rate: {percent_wins:.2f}%')
