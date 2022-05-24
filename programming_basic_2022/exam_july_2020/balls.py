import math

count_balls = int(input())
counter_red_balls = 0
counter_orange_balls = 0
counter_yellow_balls = 0
counter_white_balls = 0
other_colour_balls = 0
counter_black_balls = 0
points = 0
for balls in range(count_balls):
    colour_current_ball = input()
    if colour_current_ball == 'red':
        points += 5
        counter_red_balls += 1
    elif colour_current_ball == 'orange':
        points += 10
        counter_orange_balls += 1
    elif colour_current_ball == 'yellow':
        points += 15
        counter_yellow_balls += 1
    elif colour_current_ball == 'white':
        points += 20
        counter_white_balls += 1
    elif colour_current_ball == 'black':
        points = math.floor(points / 2)
        counter_black_balls += 1
    else:
        other_colour_balls += 1
print(f'Total points: {points}')
print(f'Red balls: {counter_red_balls}')
print(f'Orange balls: {counter_orange_balls}')
print(f'Yellow balls: {counter_yellow_balls}')
print(f'White balls: {counter_white_balls}')
print(f'Other colors picked: {other_colour_balls}')
print(f'Divides from black balls: {counter_black_balls}')



