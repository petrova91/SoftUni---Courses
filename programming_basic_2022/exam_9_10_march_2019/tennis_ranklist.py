import math

count_tournaments = int(input())
start_points = int(input())
total_points = start_points
count_wins = 0
for current_game in range(count_tournaments):
    stage_of_the_tournament = input()
    points = 0
    if stage_of_the_tournament == 'W':
        count_wins += 1
        points = 2000
    elif stage_of_the_tournament == 'F':
        points = 1200
    elif stage_of_the_tournament == 'SF':
        points = 720
    total_points += points
average_points = (total_points - start_points) / count_tournaments
percent_wins = (count_wins / count_tournaments) * 100
print(f'Final points: {total_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{percent_wins:.2f}%')

