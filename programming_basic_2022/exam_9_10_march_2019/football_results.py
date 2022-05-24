count_games = 3
count_wins = 0
count_lost = 0
count_drawn = 0
for current_game in range(count_games):
    game_result = input()
    if game_result[0] > game_result[2]:
        count_wins += 1
    elif game_result[0] < game_result[2]:
        count_lost += 1
    else:
        count_drawn += 1
print(f'Team won {count_wins} games.')
print(f'Team lost {count_lost} games.')
print(f'Drawn games: {count_drawn}')