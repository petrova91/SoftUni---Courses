def cell_code(row, col):
    position_row = {
        0: "8",
        1: "7",
        2: "6",
        3: "5",
        4: "4",
        5: "3",
        6: "2",
        7: "1",
    }
    position_col = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",
    }
    return f"{position_col[col]}{position_row[row]}"


def pawn_capture(row, col, matrix, sign, player):
    diagonals = []
    if player == "White":
        diagonals = [
            (row - 1, col - 1),
            (row - 1, col + 1)
        ]
    elif player == "Black":
        diagonals = [
            (row + 1, col - 1),
            (row + 1, col + 1)
        ]
    for diagonal in diagonals:
        row_d, col_d = diagonal
        if 0 <= row_d < len(matrix) and 0 <= col_d < len(matrix):
            if matrix[row_d][col_d] == sign:
                print(f"Game over! {player} win, capture on {cell_code(row_d, col_d)}.")
                return True
    return False


size_field = 8
field = []

white_row = ""
white_col = ""
black_row = ""
black_col = ""

for row_i in range(size_field):
    field_row = input().split()
    field.append(field_row)
    for col_i in range(size_field):
        if field[row_i][col_i] == "w":
            white_row, white_col = row_i, col_i
        elif field[row_i][col_i] == "b":
            black_row, black_col = row_i, col_i

while True:
    if pawn_capture(white_row, white_col, field, "b", "White"):
        break
    field[white_row][white_col] = "-"
    white_row -= 1
    field[white_row][white_col] = "w"
    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {cell_code(white_row, white_col)}.")
        break

    if pawn_capture(black_row, black_col, field, "w", "Black"):
        break
    field[black_row][black_col] = "-"
    black_row += 1
    field[black_row][black_col] = "b"
    if black_row == size_field - 1:
        print(f"Game over! Black pawn is promoted to a queen at {cell_code(black_row, black_col)}.")
        break