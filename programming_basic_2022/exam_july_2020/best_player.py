name_player = input()
max_count_goals = 0
best_player = ''
is_not_made_a_hat_trick = True
while name_player != 'END':
    count_goals = int(input())
    if count_goals > max_count_goals:
        max_count_goals = count_goals
        best_player = name_player
        if count_goals >= 3:
            is_not_made_a_hat_trick = False
        if count_goals >= 10:
            is_not_made_a_hat_trick = False
            break
    name_player = input()
print(f'{best_player} is the best player!')
if is_not_made_a_hat_trick:
    print(f'He has scored {max_count_goals} goals.')
else:
    print(f'He has scored {max_count_goals} goals and made a hat-trick !!!')