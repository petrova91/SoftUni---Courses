from sys import maxsize

rows, columns = [int(x) for x in input().split(", ")]
matrix = []
sub_matrix = []
max_sum = -maxsize

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

for index_row in range(rows - 1):
    for index_col in range(columns - 1):
        current_matrix = [matrix[index_row][index_col], matrix[index_row][index_col+1],
                          matrix[index_row+1][index_col], matrix[index_row+1][index_col+1]]
        sum_matrix = sum(current_matrix)
        if max_sum < sum_matrix:
            max_sum = sum_matrix
            sub_matrix = current_matrix.copy()

print(sub_matrix[0], sub_matrix[1])
print(sub_matrix[2], sub_matrix[3])
print(max_sum)



