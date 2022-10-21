def check_position(row, col, size):
    if 0 <= row < size and 0 <= col < size:
        return True
    return False


def get_count_bombs(row, col, matrix):
    bombs = 0
    neighbour_cell = [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1),
        (row - 1, col - 1),
        (row - 1, col + 1),
        (row + 1, col - 1),
        (row + 1, col + 1)
    ]
    for cell_coordinates in neighbour_cell:
        row_index = cell_coordinates[0]
        col_index = cell_coordinates[1]
        if check_position(row_index, col_index, size_field) and matrix[row_index][col_index] == "*":
            bombs += 1
    return bombs


size_field = int(input())
count_bombs = int(input())
field = []

for row_i in range(size_field):
    row_elem = []
    for col_i in range(size_field):
        row_elem.append("-")
    field.append(row_elem)

for _ in range(count_bombs):
    bomb_row, bomb_col = eval(input())
    field[bomb_row][bomb_col] = "*"

for row_i in range(size_field):
    for col_i in range(size_field):
        if field[row_i][col_i] != "*":
            field[row_i][col_i] = get_count_bombs(row_i, col_i, field)
    print(*field[row_i])