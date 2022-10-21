def sum_corresponding_nums(matrix, row, col):
    result = 0
    coordinates = [
        (0, col),
        (len(matrix) - 1, col),
        (row, 0),
        (row, len(matrix) - 1)
    ]
    for row, col in coordinates:
        result += int(matrix[row][col])
    return result


first_player, second_player = input().split(", ")
board_size = 7
board = []

for _ in range(board_size):
    board.append(input().split())

scores = {
    first_player: 501,
    second_player: 501
}
count_turn = 1
players = [first_player, second_player]

while True:
    player = players[0]
    player_row, player_col = eval(input())

    if 0 <= player_row < board_size and 0 <= player_col < board_size:
        if board[player_row][player_col].isdigit():
            scores[player] -= int(board[player_row][player_col])
        elif board[player_row][player_col] == "D":
            sum_nums = sum_corresponding_nums(board, player_row, player_col)
            scores[player] -= sum_nums * 2
        elif board[player_row][player_col] == "T":
            sum_nums = sum_corresponding_nums(board, player_row, player_col)
            scores[player] -= sum_nums * 3
        elif board[player_row][player_col] == "B":
            print(f"{player} won the game with {count_turn} throws!")
            break

    if scores[player] <= 0:
        print(f"{player} won the game with {count_turn} throws!")
        break

    players[0], players[1] = players[1], players[0]
    if player == second_player:
        count_turn += 1