first_player_name = input()
second_player_name = input()
first_player_points = 0
second_player_points = 0
winner_name = ''
winner_points = ''
number_wars = False
first_player_card = input()
while first_player_card != 'End of game':
    first_player_card = int(first_player_card)
    second_player_card = int(input())
    if first_player_card > second_player_card:
        points = first_player_card - second_player_card
        first_player_points += points
    elif first_player_card < second_player_card:
        points = second_player_card - first_player_card
        second_player_points += points
    elif first_player_card == second_player_card:
        number_wars = True
        one_more_card_first_player = int(input())
        one_more_card_second_player = int(input())
        if one_more_card_first_player > one_more_card_second_player:
            winner_name = first_player_name
            winner_points = first_player_points
        else:
            winner_name = second_player_name
            winner_points = second_player_points
        break
    first_player_card = input()
if number_wars:
    print('Number wars!')
    print(f'{winner_name} is winner with {winner_points} points')
else:
    print(f'{first_player_name} has {first_player_points} points')
    print(f'{second_player_name} has {second_player_points} points')

