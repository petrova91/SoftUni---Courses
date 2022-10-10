import re


def get_next_position(row, col, direction):
    if direction == "up":
        return row-1, col
    elif direction == "down":
        return row+1, col
    elif direction == "left":
        return row, col-1
    elif direction == "right":
        return row, col+1


size_matrix = 6
table = []

for _ in range(size_matrix):
    table.append(list(input().split()))

start_position = input()
pattern = r"\d+"
current_row, current_col = [int(x) for x in re.findall(pattern, start_position)]

command = input()
while not command == "Stop":
    data = command.split(", ")
    name_command, direction = data[0], data[1]

    if name_command == "Create":
        value = data[2]
        current_row, current_col = get_next_position(current_row, current_col, direction)
        if table[current_row][current_col] == ".":
            table[current_row][current_col] = value

    elif name_command == "Update":
        value = data[2]
        current_row, current_col = get_next_position(current_row, current_col, direction)
        if table[current_row][current_col] != ".":
            table[current_row][current_col] = value

    elif name_command == "Delete":
        current_row, current_col = get_next_position(current_row, current_col, direction)
        if table[current_row][current_col] != ".":
            table[current_row][current_col] = "."

    elif name_command == "Read":
        current_row, current_col = get_next_position(current_row, current_col, direction)
        if table[current_row][current_col] != ".":
            print(table[current_row][current_col])

    command = input()

for row_i in table:
    print(*row_i)