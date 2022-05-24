number_balls = int(input())
counter_levels = 0
counter_balls = 0
balls_are_finish = False
for rows in range(1, number_balls+1):
    counter_levels += 1
    for colons in range(1, rows+1):
        counter_balls += 1
        if counter_balls > number_balls:
            balls_are_finish = True
            counter_levels -= 1
            break
    if balls_are_finish:
        break
print(f'pyramid({number_balls}) == {counter_levels}')