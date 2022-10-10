rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for index in range(rows):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][rows - 1 - index])

different = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(different)