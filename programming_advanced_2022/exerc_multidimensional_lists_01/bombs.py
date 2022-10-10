from collections import deque


def check_index(index, count_rows):
    if 0 <= index < count_rows:
        return True
    return False


rows = int(input())
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

bombs = deque(input().split())

while bombs:
    bomb_coordinates = bombs.popleft()
    bomb_row, bomb_col = [int(x) for x in bomb_coordinates.split(",")]
    bomb_value = matrix[bomb_row][bomb_col]
    if bomb_value <= 0:
        continue
    matrix[bomb_row][bomb_col] = 0

    if check_index(bomb_col-1, rows) and matrix[bomb_row][bomb_col-1] > 0:
        matrix[bomb_row][bomb_col-1] -= bomb_value
    if check_index(bomb_col+1, rows) and matrix[bomb_row][bomb_col+1] > 0:
        matrix[bomb_row][bomb_col+1] -= bomb_value
    if check_index(bomb_row-1, rows):
        if check_index(bomb_col-1, rows) and matrix[bomb_row-1][bomb_col-1] > 0:
            matrix[bomb_row-1][bomb_col-1] -= bomb_value
        if check_index(bomb_col, rows) and matrix[bomb_row-1][bomb_col] > 0:
            matrix[bomb_row-1][bomb_col] -= bomb_value
        if check_index(bomb_col+1, rows) and matrix[bomb_row-1][bomb_col+1] > 0:
            matrix[bomb_row-1][bomb_col+1] -= bomb_value
    if check_index(bomb_row+1, rows):
        if check_index(bomb_col-1, rows) and matrix[bomb_row+1][bomb_col-1] > 0:
            matrix[bomb_row+1][bomb_col-1] -= bomb_value
        if check_index(bomb_col, rows) and matrix[bomb_row+1][bomb_col] > 0:
            matrix[bomb_row+1][bomb_col] -= bomb_value
        if check_index(bomb_col+1, rows) and matrix[bomb_row+1][bomb_col+1] > 0:
            matrix[bomb_row+1][bomb_col+1] -= bomb_value

alive_cells = 0
sum_cells = 0
for row_i in range(rows):
    for col_i in range(rows):
        if matrix[row_i][col_i] > 0:
            alive_cells += 1
            sum_cells += matrix[row_i][col_i]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_cells}")

for i in range(rows):
    print(*matrix[i])

