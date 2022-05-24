first_player_count_eggs = int(input())
second_player_count_eggs = int(input())
winner = input()
first_player_is_winner = False
second_player_is_winner = False
while winner != 'End':
    if winner == 'one':
        second_player_count_eggs -= 1
        if second_player_count_eggs == 0:
            second_player_is_winner = True
            break
    else:
        first_player_count_eggs -= 1
        if first_player_count_eggs == 0:
            first_player_is_winner = True
            break
    winner = input()
if first_player_is_winner:
    print(f'Player one is out of eggs. Player two has {second_player_count_eggs} eggs left.')
elif second_player_is_winner:
    print(f'Player two is out of eggs. Player one has {first_player_count_eggs} eggs left.')
else:
    print(f'Player one has {first_player_count_eggs} eggs left.')
    print(f'Player two has {second_player_count_eggs} eggs left.')