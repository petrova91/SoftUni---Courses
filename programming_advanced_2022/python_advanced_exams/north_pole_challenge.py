def check_index(row, col, count_rows, count_cols):
    if row < 0:
        row = count_rows - 1
    elif row == count_rows:
        row = 0
    if col < 0:
        col = count_cols - 1
    elif col == count_cols:
        col = 0
    return row, col


def get_position(direction, row, col):
    if direction == "right":
        return check_index(row, col + 1, rows, columns)
    elif direction == "left":
        return check_index(row, col - 1, rows, columns)
    elif direction == "up":
        return check_index(row - 1, col, rows, columns)
    elif direction == "down":
        return check_index(row + 1, col, rows, columns)


def check_collect_items(matrix, count_rows, count_cols):
    items = ["D", "G", "C"]
    for index_row in range(count_rows):
        for index_col in range(count_cols):
            if matrix[index_row][index_col] in items:
                return False
    return True


rows, columns = [int(x) for x in input().split(", ")]
player_row = ""
player_col = ""
shop = []
collected_items = {
    "Christmas decorations": 0,
    "Gifts": 0,
    "Cookies": 0
}

for row_i in range(rows):
    shop.append(input().split())
    for col_i in range(columns):
        if shop[row_i][col_i] == "Y":
            player_row, player_col = row_i, col_i

shop[player_row][player_col] = "x"
items_are_collect = False

command = input()
while not command == "End":
    direction, steps = command.split("-")
    steps = int(steps)

    for _ in range(steps):
        shop[player_row][player_col] = "x"
        player_row, player_col = get_position(direction, player_row, player_col)
        if shop[player_row][player_col] == "D":
            collected_items["Christmas decorations"] += 1
        elif shop[player_row][player_col] == "G":
            collected_items["Gifts"] += 1
        elif shop[player_row][player_col] == "C":
            collected_items["Cookies"] += 1
        shop[player_row][player_col] = "Y"
        if check_collect_items(shop, rows, columns):
            print("Merry Christmas!")
            items_are_collect = True
            break
    if items_are_collect:
        break
    command = input()

print("You've collected:")
for item, quantity in collected_items.items():
    print(f"- {quantity} {item}")
for i in range(rows):
    print(*shop[i])