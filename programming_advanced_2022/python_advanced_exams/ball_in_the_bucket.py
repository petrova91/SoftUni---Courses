import re


def sum_columns_points(col, matrix):
    sum_points = 0
    for i in range(len(matrix)):
        if matrix[i][col].isdigit():
            sum_points += int(matrix[i][col])
    return sum_points


def get_prize(points):
    if 100 <= points <= 199:
        return f"Good job! You scored {points} points, and you've won Football."
    elif 200 <= points <= 299:
        return f"Good job! You scored {points} points, and you've won Teddy Bear."
    elif 300 <= points <= 399:
        return f"Good job! You scored {points} points, and you've won Lego Construction Set."
    return f"Sorry! You need {100 - points} points more to win a prize."


size = 6
count_shoots = 3
score = 0

pattern = r"\d+"

board = []
for row_i in range(size):
    row_elem = input().split()
    board.append(row_elem)

for _ in range(count_shoots):
    coordinates = input()
    shoot_row, shoot_col = [int(x) for x in re.findall(pattern, coordinates)]
    if 0 <= shoot_row < size and 0 <= shoot_col < size:
        if board[shoot_row][shoot_col] == "B":
            score += sum_columns_points(shoot_col, board)
            board[shoot_row][shoot_col] = "X"

print(get_prize(score))