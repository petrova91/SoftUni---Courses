from math import floor


def get_next_position(row, col, destination):
    if destination == "up":
        return check_index(row - 1, col, size_board)
    elif destination == "down":
        return check_index(row + 1, col, size_board)
    elif destination == "left":
        return check_index(row, col - 1, size_board)
    elif destination == "right":
        return check_index(row, col + 1, size_board)
    else:
        return row, col


def check_index(row, col, size):
    if row < 0:
        row = size - 1
    elif col < 0:
        col = size - 1
    elif row == size:
        row = 0
    elif col == size:
        col = 0
    return row, col


size_board = int(input())
board = []
path_sign = "."
player_row = 0
player_col = 0

for row_i in range(size_board):
    row_elem = input().split()
    board.append(row_elem)
    if "P" in row_elem:
        player_row = row_i
        player_col = row_elem.index("P")

coins = 0
player_path = list()
player_path.append(f"[{player_row}, {player_col}]")
board[player_row][player_col] = path_sign
while True:
    command = input()
    player_row, player_col = get_next_position(player_row, player_col, command)
    player_path.append(f"[{player_row}, {player_col}]")
    if board[player_row][player_col].isdigit():
        coins += int(board[player_row][player_col])
        board[player_row][player_col] = path_sign
    elif board[player_row][player_col] == "X":
        coins /= 2
        coins = floor(coins)
        print(f"Game over! You've collected {coins} coins.")
        break

    if coins >= 100:
        print(f"You won! You've collected {coins} coins.")
        break

print("Your path:")
for position in player_path:
    print(position)