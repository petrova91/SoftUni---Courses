def get_next_position(row, col, direction):
    if direction == "up":
        return row-1, col
    elif direction == "down":
        return row+1, col
    elif direction == "left":
        return row, col-1
    elif direction == "right":
        return row, col+1


def is_inside(row, col, max_size):
    if 0 <= row < max_size and 0 <= col < max_size:
        return True
    return False


def give_presents(row, col, matrix, count_presents, nice_kids):
    possible_moves = [
        [row-1, col],
        [row+1, col],
        [row, col+1],
        [row, col-1]
    ]
    for current_row, current_col in possible_moves:
        if matrix[current_row][current_col] != "-":
            count_presents -= 1
            if matrix[current_row][current_col] == "V":
                nice_kids -= 1
        matrix[current_row][current_col] = "-"
    return count_presents, nice_kids, matrix


presents = int(input())
size = int(input())
matrix = []
santa_row = 0
santa_col = 0
count_nice_kids = 0

for row_i in range(size):
    row_elem = input().split()
    matrix.append(row_elem)
    if "S" in row_elem:
        santa_row = row_i
        santa_col = row_elem.index("S")
    if "V" in row_elem:
        count_nice_kids += row_elem.count("V")

kids_with_present = count_nice_kids
matrix[santa_row][santa_col] = "-"
command = input()
while not command == "Christmas morning":
    next_row, next_col = get_next_position(santa_row, santa_col, command)
    if not is_inside(next_row, next_col, size):
        command = input()
        continue
    santa_row = next_row
    santa_col = next_col
    if matrix[santa_row][santa_col] == "X":
        matrix[santa_row][santa_col] = "-"
    elif matrix[santa_row][santa_col] == "V":
        presents -= 1
        count_nice_kids -= 1
        matrix[santa_row][santa_col] = "-"
    elif matrix[santa_row][santa_col] == "C":
        presents, count_nice_kids, matrix = give_presents(santa_row, santa_col, matrix, presents, count_nice_kids)
    if presents == 0:
        break
    command = input()

matrix[santa_row][santa_col] = "S"
if presents == 0 and count_nice_kids > 0:
    print("Santa ran out of presents!")
for i in range(size):
    print(*matrix[i])
if count_nice_kids == 0:
    print(f"Good job, Santa! {kids_with_present} happy nice kid/s.")
else:
    print(f"No presents for {count_nice_kids} nice kid/s.")