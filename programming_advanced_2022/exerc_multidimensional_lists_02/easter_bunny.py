from sys import maxsize


def get_children(row, col, max_size):
    children = []
    possible_children = [
        [row-1, col],
        [row, col+1],
        [row+1, col],
        [row, col-1]
    ]
    for row_index, col_index in possible_children:
        if 0 <= row_index < max_size and 0 <= col_index < max_size:
            children.append([row_index, col_index])
    return children


def move_same_row(start, end, step, matrix, row):
    sum_eggs = 0
    coordinates = []
    for i in range(start, end, step):
        if not matrix[row][i] == "X":
            sum_eggs += int(matrix[row][i])
            coordinates.append([row, i])
        else:
            break
    return sum_eggs, coordinates


def move_same_col(start, end, step, matrix, col):
    sum_eggs = 0
    coordinates = []
    for i in range(start, end, step):
        if not matrix[i][col] == "X":
            sum_eggs += int(matrix[i][col])
            coordinates.append([i, col])
        else:
            break
    return sum_eggs, coordinates


size = int(input())
field = []
bunny_row = None
bunny_col = None
total_eggs = -maxsize
direction = ""
eggs_positions = []

for row_i in range(size):
    current_row = input().split()
    field.append(current_row)
    if "B" in current_row:
        bunny_row = row_i
        bunny_col = current_row.index("B")

possible_moves = get_children(bunny_row, bunny_col, size)
for row_i, col_i in possible_moves:
    total_sum = 0
    current_move = ""
    moves = []
    if col_i == bunny_col+1:
        current_move = "right"
        total_sum, moves = move_same_row(col_i, size, 1, field, row_i)
    elif col_i == bunny_col-1:
        current_move = "left"
        total_sum, moves = move_same_row(col_i, -1, -1, field, row_i)
    elif row_i == bunny_row-1:
        current_move = "up"
        total_sum, moves = move_same_col(row_i, -1, -1, field, col_i)
    elif row_i == bunny_row+1:
        current_move = "down"
        total_sum, moves = move_same_col(row_i, size, 1, field, col_i)
    if total_sum > total_eggs and moves:
        total_eggs = total_sum
        direction = current_move
        eggs_positions = moves

print(direction)
print(*eggs_positions, sep="\n")
print(total_eggs)