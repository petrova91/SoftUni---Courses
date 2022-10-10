rows, columns = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    row = input().split()
    matrix.append(row)

command = input()
while not command == "END":
    invalid_command = False
    data = command.split()
    if not data[0] == "swap" or len(data) != 5:
        invalid_command = True
    else:
        row_1 = int(data[1])
        col_1 = int(data[2])
        row_2 = int(data[3])
        col_2 = int(data[4])
        if 0 <= row_1 < rows and 0 <= row_2 < rows and 0 <= col_1 < columns and 0 <= col_2 < columns:
            elem = matrix[row_1][col_1]
            matrix[row_1][col_1] = matrix[row_2][col_2]
            matrix[row_2][col_2] = elem
            for i in range(rows):
                print(" ".join(matrix[i]))
        else:
            invalid_command = True
    if invalid_command:
        print("Invalid input!")
    command = input()