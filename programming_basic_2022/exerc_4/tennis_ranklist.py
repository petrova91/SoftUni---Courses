import math

count_competition = int(input())
count_points = int(input())
count_win = 0
points = 0
for current_competition in range(count_competition):
    position = input()
    if position == 'W':
        points += 2000
        count_win += 1
    elif position == 'F':
        points += 1200
    elif position == 'SF':
        points += 720
middle_points = points / count_competition
percent_win = (count_win / count_competition) * 100
total_points = count_points + points
print(f'Final points: {total_points}')
print(f'Average points: {math.floor(middle_points)}')
print(f'{percent_win:.2f}%')

