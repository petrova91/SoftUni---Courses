def is_inside(row, col, max_size):
    if 0 <= row < max_size and 0 <= col < max_size:
        return True
    return False


def possible_knights(row, col, matrix):
    knights = 0
    moves = [
        [row-2, col+1],
        [row-2, col-1],
        [row-1, col+2],
        [row-1, col-2],
        [row+1, col+2],
        [row+1, col-2],
        [row+2, col+1],
        [row+2, col-1]
    ]
    for row_index, col_index in moves:
        if is_inside(row_index, col_index, size) and matrix[row_index][col_index] == "K":
            knights += 1
    return knights


size = int(input())
field = []
removed_knights = 0

for row_i in range(size):
    row_element = list(input())
    field.append(row_element)

while True:
    max_knights_places = 0
    knight_row = 0
    knight_col = 0
    for row_index in range(size):
        for col_index in range(size):
            if field[row_index][col_index] == "0":
                continue
            knights_counter = possible_knights(row_index, col_index, field)
            if knights_counter > max_knights_places:
                max_knights_places = knights_counter
                knight_row = row_index
                knight_col = col_index
    if max_knights_places > 0:
        field[knight_row][knight_col] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
