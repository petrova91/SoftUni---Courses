def get_next_position(row, col, direction):
    if direction == "up":
        return row - 1, col
    elif direction == "down":
        return row + 1, col
    elif direction == "left":
        return row, col - 1
    elif direction == "right":
        return row, col + 1


size_board = int(input())
board = []

snake_row = None
snake_col = None
burrows = []

for row_i in range(size_board):
    row_elem = list(input())
    board.append(row_elem)
    for col_i in range(size_board):
        if board[row_i][col_i] == "S":
            snake_row, snake_col = row_i, col_i
        if board[row_i][col_i] == "B":
            burrow_row, burrow_col = row_i, col_i
            burrows.append((burrow_row, burrow_col))

food = 0
board[snake_row][snake_col] = "."
while True:
    command = input()
    board[snake_row][snake_col] = "."
    snake_row, snake_col = get_next_position(snake_row, snake_col, command)
    if snake_row < 0 or snake_row == size_board or snake_col < 0 or snake_col == size_board:
        print("Game over!")
        break

    if board[snake_row][snake_col] == "*":
        food += 1
        board[snake_row][snake_col] = "S"
        if food == 10:
            print("You won! You fed the snake.")
            break

    elif board[snake_row][snake_col] == "B":
        board[snake_row][snake_col] = "."
        for burrow_coordinates in burrows:
            if snake_row != burrow_coordinates[0] and snake_col != burrow_coordinates[1]:
                snake_row, snake_col = burrow_coordinates[0], burrow_coordinates[1]

    board[snake_row][snake_col] = "S"

print(f"Food eaten: {food}")
for i in range(size_board):
    print(*board[i], sep="")