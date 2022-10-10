import re

first_player, second_player = input().split(", ")

rows = 6
columns = 6
field = []
for row_i in range(rows):
    field.append(input().split())

player_counter = 0
player_in_rest = {}
while True:
    pattern = r"\d+"
    player_coordinates = input()
    player_row, player_col = [int(x) for x in re.findall(pattern, player_coordinates)]

    player_counter += 1
    player = first_player if player_counter % 2 != 0 else second_player

    if player in player_in_rest and player_in_rest[player] > player_counter:
        player_in_rest.pop(player)
    elif player in player_in_rest and player_in_rest[player] == player_counter:
        continue

    if field[player_row][player_col] == "E":
        print(f"{player} found the Exit and wins the game!")
        break

    elif field[player_row][player_col] == "T":
        player_counter += 1
        winner = first_player if player_counter % 2 != 0 else second_player
        print(f"{player} is out of the game! The winner is {winner}.")
        break

    elif field[player_row][player_col] == "W":
        player_in_rest[player] = player_counter + 2
        print(f"{player} hits a wall and needs to rest.")