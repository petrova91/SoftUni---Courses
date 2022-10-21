def check_up_direction(row, col, matrix, queens_position):
    for row_index in range(row-1, -1, -1):
        if matrix[row_index][col] == "Q":
            queens_position.append(f"[{row_index}, {col}]")
            return True
    return False


def check_down_direction(row, col, matrix, queens_position):
    for row_index in range(row+1, len(matrix)):
        if matrix[row_index][col] == "Q":
            queens_position.append(f"[{row_index}, {col}]")
            return True
    return False


def check_right_direction(row, col, matrix, queens_position):
    for col_index in range(col+1, len(matrix)):
        if matrix[row][col_index] == "Q":
            queens_position.append(f"[{row}, {col_index}]")
            return True
    return False


def check_left_direction(row, col, matrix, queens_position):
    for col_index in range(col-1, -1, -1):
        if matrix[row][col_index] == "Q":
            queens_position.append(f"[{row}, {col_index}]")
            return True
    return False


def check_player_on_board(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def check_up_left_diagonal(row, col, matrix, queens_position):
    for _ in range(len(matrix)):
        row -= 1
        col -= 1
        if not check_player_on_board(row, col, size_board):
            return False
        else:
            if matrix[row][col] == "Q":
                queens_position.append(f"[{row}, {col}]")
                return True


def check_down_left_diagonal(row, col, matrix, queens_position):
    for _ in range(len(matrix)):
        row += 1
        col -= 1
        if not check_player_on_board(row, col, size_board):
            return False
        else:
            if matrix[row][col] == "Q":
                queens_position.append(f"[{row}, {col}]")
                return True


def check_up_right_diagonal(row, col, matrix, queens_position):
    for _ in range(len(matrix)):
        row -= 1
        col += 1
        if not check_player_on_board(row, col, size_board):
            return False
        else:
            if matrix[row][col] == "Q":
                queens_position.append(f"[{row}, {col}]")
                return True


def check_down_right_diagonal(row, col, matrix, queens_position):
    for _ in range(len(matrix)):
        row += 1
        col += 1
        if not check_player_on_board(row, col, size_board):
            return False
        else:
            if matrix[row][col] == "Q":
                queens_position.append(f"[{row}, {col}]")
                return True


size_board = 8
board = []
queens = []

king_row = 0
king_col = 0

for row_i in range(size_board):
    row_elem = input().split()
    board.append(row_elem)
    if "K" in row_elem:
        king_row = row_i
        king_col = row_elem.index("K")

if any([
    check_up_direction(king_row, king_col, board, queens),
    check_down_direction(king_row, king_col, board, queens),
    check_right_direction(king_row, king_col, board, queens),
    check_left_direction(king_row, king_col, board, queens),
    check_up_right_diagonal(king_row, king_col, board, queens),
    check_up_left_diagonal(king_row, king_col, board, queens),
    check_down_right_diagonal(king_row, king_col, board, queens),
    check_down_left_diagonal(king_row, king_col, board, queens)
]):
    print(*queens, sep="\n")
else:
    print("The king is safe!")
