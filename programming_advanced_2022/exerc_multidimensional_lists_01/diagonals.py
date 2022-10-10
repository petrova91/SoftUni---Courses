rows = int(input())
matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(rows):
    row = [int(x) for x in input().split(", ")]
    matrix.append(row)

for index in range(rows):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][rows - 1 - index])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
