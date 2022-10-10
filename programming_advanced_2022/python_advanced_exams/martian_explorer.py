def move_up(row, col):
    row -= 1
    return check_position(row, col, size_matrix)


def move_down(row, col):
    row += 1
    return check_position(row, col, size_matrix)


def move_left(row, col):
    col -= 1
    return check_position(row, col, size_matrix)


def move_right(row, col):
    col += 1
    return check_position(row, col, size_matrix)


def check_position(row, col, size):
    if row < 0:
        row = size - 1
    elif col < 0:
        col = size - 1
    elif row == size:
        row = 0
    elif col == size:
        col = 0
    return row, col


size_matrix = 6
area = []
rover_row = None
rover_col = None

for row_i in range(size_matrix):
    row_elem = list(input().split())
    area.append(row_elem)
    if "E" in row_elem:
        rover_row = row_i
        rover_col = row_elem.index("E")

directions = {
    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right
}
deposits = {
    "W": "Water",
    "M": "Metal",
    "C": "Concrete"
}

found_deposits = set()
commands = input().split(", ")
for command in commands:
    rover_row, rover_col = directions[command](rover_row, rover_col)
    if area[rover_row][rover_col] in deposits:
        deposit = area[rover_row][rover_col]
        found_deposits.add(deposit)
        print(f"{deposits[deposit]} deposit found at ({rover_row}, {rover_col})")

    elif area[rover_row][rover_col] == "R":
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        break

if len(found_deposits) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")