from sys import maxsize

rows, columns = [int(x) for x in input().split()]
matrix = []
max_sum = -maxsize
sub_matrix = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for row_index in range(rows-2):
    for col_index in range(columns-2):
        current_matrix = [matrix[row_index][col_index], matrix[row_index][col_index+1], matrix[row_index][col_index+2],
                          matrix[row_index+1][col_index], matrix[row_index+1][col_index+1], matrix[row_index+1][col_index+2],
                          matrix[row_index+2][col_index], matrix[row_index+2][col_index+1], matrix[row_index+2][col_index+2]]
        sum_matrix = sum(current_matrix)
        if sum_matrix > max_sum:
            max_sum = sum_matrix
            sub_matrix = current_matrix.copy()

print(f"Sum = {max_sum}")
print(sub_matrix[0], sub_matrix[1], sub_matrix[2])
print(sub_matrix[3], sub_matrix[4], sub_matrix[5])
print(sub_matrix[6], sub_matrix[7], sub_matrix[8])