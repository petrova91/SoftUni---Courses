rows, columns = [int(x) for x in input().split()]
matrix = []

for row_index in range(rows):
    current_row = []
    for col_index in range(columns):
        first_letter = chr(97+row_index)
        second_letter = chr(97 + row_index + col_index)
        elem = first_letter + second_letter + first_letter
        current_row.append(elem)
    matrix.append(current_row)

for i in range(len(matrix)):
    print(" ".join(matrix[i]))