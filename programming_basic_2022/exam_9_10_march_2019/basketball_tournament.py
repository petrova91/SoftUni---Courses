name_tournament = input()
count_wins = 0
count_lost = 0
count_total_games = 0
while name_tournament != 'End of tournaments':
    count_games = int(input())
    count_total_games += count_games
    for current_game in range(1, count_games+1):
        points_desi_team = int(input())
        other_team_points = int(input())
        if points_desi_team > other_team_points:
            count_wins += 1
            different_points = points_desi_team - other_team_points
            print(f'Game {current_game} of tournament {name_tournament}: win with {different_points} points.')
        else:
            count_lost += 1
            different_points = other_team_points - points_desi_team
            print(f'Game {current_game} of tournament {name_tournament}: lost with {different_points} points.')
    name_tournament = input()
percent_wins = (count_wins / count_total_games) * 100
percent_lost = (count_lost / count_total_games) * 100
print(f'{percent_wins:.2f}% matches win')
print(f'{percent_lost:.2f}% matches lost')