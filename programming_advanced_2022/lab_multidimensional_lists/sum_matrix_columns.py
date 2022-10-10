rows, columns = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for col_index in range(columns):
    sum_column = 0
    for row_index in range(rows):
        sum_column += matrix[row_index][col_index]
    print(sum_column)