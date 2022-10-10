count_rows = int(input())
matrix = []

for _ in range(count_rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

command = input()
while not command == "END":
    name_command, row_i, col_i, value = command.split()
    row_i = int(row_i)
    col_i = int(col_i)
    value = int(value)
    if (len(matrix) <= row_i or row_i < 0) or (len(matrix) <= col_i or col_i < 0):
        print("Invalid coordinates")
        command = input()
        continue
    if name_command == "Add":
        matrix[row_i][col_i] += value
    elif name_command == "Subtract":
        matrix[row_i][col_i] -= value
    command = input()

for i in range(len(matrix)):
    print(*matrix[i])