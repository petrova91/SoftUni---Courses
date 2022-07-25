def add_player(players_dict, data):
    player, position, skill = data.split(' -> ')
    skill = int(skill)
    if player not in players_dict:
        players_dict[player] = {}
    if position not in players_dict[player]:
        players_dict[player][position] = skill
    else:
        if skill > players_dict[player][position]:
            players_dict[player][position] = skill
    return players_dict


def duel_battle(players, data):
    winner_is_found = False
    first_player, second_player = data.split(' vs ')
    if first_player in players and second_player in players:
        for first_player_position, first_player_points in players[first_player].items():
            for second_player_position, second_player_points in players[second_player].items():
                if first_player_position == second_player_position:
                    if sum(players[first_player].values()) > sum(players[second_player].values()):
                        players.pop(second_player)
                    elif sum(players[first_player].values()) < sum(players[second_player].values()):
                        players.pop(first_player)
                    winner_is_found = True
                    break
            if winner_is_found:
                break
    return players


command = input()
users = {}
best_players = {}
while command != 'Season end':
    if '->' in command:
        users = add_player(users, command)
    elif 'vs' in command:
        users = duel_battle(users, command)
    command = input()
# for user, scores in users.items():
#     best_players[user] = sum(users[user].values())
# ordered_player = dict(sorted(best_players.items(), key=lambda x: (-x[1], x[0])))
# for player in ordered_player:
#     print(f"{player}: {best_players[player]} skill")
#     for user, scores in users.items():
#         if user == player:
#             for position, points in sorted(scores.items(), key=lambda x: (-x[1], x[0])):
#                 print(f"- {position} <::> {points}")
for player, score in sorted(users.items(), key=lambda x: (-sum(x[1].values()), x[0])):
    print(f"{player}: {sum(score.values())} skill")
    for skill, value in sorted(score.items(), key=lambda x: (-x[1], x[0])):
        print(f"- {skill} <::> {value}")
