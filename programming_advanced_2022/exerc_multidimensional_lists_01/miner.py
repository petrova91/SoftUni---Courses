from collections import deque


def check_index(i, count_rows):
    if 0 <= i < count_rows:
        return True
    return False


def move_left(column):
    index = column - 1
    if check_index(index, rows):
        return index
    return column


def move_right(column):
    index = column + 1
    if check_index(index, rows):
        return index
    return column


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


rows = int(input())
commands = deque(input().split())
field = []
row_i = None
col_i = None
coal = 0

for row_index in range(rows):
    current_row = [x for x in input().split()]
    if "s" in current_row:
        row_i = row_index
        col_i = current_row.index("s")
    if "c" in current_row:
        coal += current_row.count("c")
    field.append(current_row)

while commands:
    command = commands.popleft()
    if command == "left":
        col_i = move_left(col_i)
    elif command == "right":
        col_i = move_right(col_i)
    elif command == "up":
        row_i = move_up(row_i)
    elif command == "down":
        row_i = move_down(row_i)
    if field[row_i][col_i] == "c":
        coal -= 1
        field[row_i][col_i] = "*"
        if coal == 0:
            print(f"You collected all coal! ({row_i}, {col_i})")
            break
    elif field[row_i][col_i] == "e":
        print(f"Game over! ({row_i}, {col_i})")
        break
else:
    print(f"{coal} pieces of coal left. ({row_i}, {col_i})")