rows = int(input())
matrix = []
diagonal_sum = 0

for _ in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

for index in range(rows):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)