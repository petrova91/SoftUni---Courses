count_games = int(input())
count_hearthstone = 0
count_fornite = 0
count_overwatch = 0
count_others_game = 0
for current_games in range(count_games):
    game_name = input()
    if game_name == 'Hearthstone':
        count_hearthstone += 1
    elif game_name == 'Fornite':
        count_fornite += 1
    elif game_name == 'Overwatch':
        count_overwatch += 1
    else:
        count_others_game += 1
percent_hearthstone = (count_hearthstone / count_games) * 100
percent_fornite = (count_fornite / count_games) * 100
percent_overwatch = (count_overwatch / count_games) * 100
percent_other_game = (count_others_game / count_games) * 100
print(f'Hearthstone - {percent_hearthstone:.2f}%')
print(f'Fornite - {percent_fornite:.2f}%')
print(f'Overwatch - {percent_overwatch:.2f}%')
print(f'Others - {percent_other_game:.2f}%')


