from collections import deque
from copy import deepcopy


def check_index(index, max_value):
    if 0 <= index < max_value:
        return True
    return False


def move_up(row):
    index = row - 1
    if check_index(index, rows):
        return index
    return row


def move_down(row):
    index = row + 1
    if check_index(index, rows):
        return index
    return row


def move_left(col):
    index = col - 1
    if check_index(index, columns):
        return index
    return col


def move_right(col):
    index = col + 1
    if check_index(index, columns):
        return index
    return col


def bunny_spread(matrix):
    sub_matrix = deepcopy(matrix)
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            if matrix[row_index][col_index] == "B":
                down_index = move_down(row_index)
                sub_matrix[down_index][col_index] = "B"
                up_index = move_up(row_index)
                sub_matrix[up_index][col_index] = "B"
                left_index = move_left(col_index)
                sub_matrix[row_index][left_index] = "B"
                right_index = move_right(col_index)
                sub_matrix[row_index][right_index] = "B"
    return sub_matrix


def check_for_player(matrix):
    for row_index in range(len(matrix)):
        if "P" in matrix[row_index]:
            return True
    return False


rows, columns = [int(x) for x in input().split()]
lair = []
players_row = None
players_col = None
player_win = False

for i in range(rows):
    current_row = [x for x in input()]
    lair.append(current_row)
    if "P" in current_row:
        players_col = current_row.index("P")
        players_row = i

commands = deque([x for x in input()])

while True:
    command = commands.popleft()
    last_player_row = players_row
    last_player_col = players_col
    lair[players_row][players_col] = "."
    if command == "L":
        players_col = move_left(players_col)
    elif command == "R":
        players_col = move_right(players_col)
    elif command == "U":
        players_row = move_up(players_row)
    elif command == "D":
        players_row = move_down(players_row)

    if last_player_row == players_row and last_player_col == players_col:
        lair = bunny_spread(lair)
        player_win = True
        break
    elif lair[players_row][players_col] == "B":
        lair = bunny_spread(lair)
        break

    lair[players_row][players_col] = "P"
    lair = bunny_spread(lair)
    if not check_for_player(lair):
        break

for index in range(rows):
    print("".join(lair[index]))
if player_win:
    print(f"won: {players_row} {players_col}")
else:
    print(f"dead: {players_row} {players_col}")