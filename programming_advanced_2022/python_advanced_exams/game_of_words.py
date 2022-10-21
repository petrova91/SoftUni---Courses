def get_next_position(row, col, destination):
    if destination == "up":
        return row - 1, col
    elif destination == "down":
        return row + 1, col
    elif destination == "left":
        return row, col - 1
    elif destination == "right":
        return row, col + 1


def check_player_on_board(row, col, matrix):
    if row < 0 or col < 0 or row == len(matrix) or col == len(matrix):
        return False
    return True


some_text = input()
size_board = int(input())
board = []

player_row = 0
player_col = 0
for row_i in range(size_board):
    row_elem = list(input())
    board.append(row_elem)
    if "P" in row_elem:
        player_row = row_i
        player_col = row_elem.index("P")

count_commands = int(input())
for _ in range(count_commands):
    command = input()
    board[player_row][player_col] = "-"
    next_player_row, next_player_col = get_next_position(player_row, player_col, command)
    if check_player_on_board(next_player_row, next_player_col, board):
        player_row, player_col = next_player_row, next_player_col
    else:
        if some_text:
            some_text = some_text[:-1]

    if board[player_row][player_col].isalpha():
        some_text += board[player_row][player_col]

    board[player_row][player_col] = "P"

print(some_text)
for i in range(size_board):
    print(*board[i], sep="")