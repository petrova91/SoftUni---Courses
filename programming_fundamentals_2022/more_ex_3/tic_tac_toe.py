def check_winner(game_field, player):
    player_is_win = False
    if game_field[0][0] == game_field[0][1] == game_field[0][2] == player:
        player_is_win = True
    elif game_field[1][0] == game_field[1][1] == game_field[1][2] == player:
        player_is_win = True
    elif game_field[2][0] == game_field[2][1] == game_field[2][2] == player:
        player_is_win = True
    elif game_field[0][0] == game_field[1][0] == game_field[2][0] == player:
        player_is_win = True
    elif game_field[0][1] == game_field[1][1] == game_field[2][1] == player:
        player_is_win = True
    elif game_field[0][2] == game_field[1][2] == game_field[2][2] == player:
        player_is_win = True
    elif game_field[0][0] == game_field[1][1] == game_field[2][2] == player:
        player_is_win = True
    elif game_field[0][2] == game_field[1][1] == game_field[2][0] == player:
        player_is_win = True
    return player_is_win


number_rows = 3
field = []
first_player = '1'
second_player = '2'
for current_row in range(number_rows):
    row = input().split()
    field.append(row)
first_player_is_winner = check_winner(field, first_player)
second_player_is_winner = check_winner(field, second_player)
if first_player_is_winner:
    print('First player won')
elif second_player_is_winner:
    print('Second player won')
else:
    print('Draw!')