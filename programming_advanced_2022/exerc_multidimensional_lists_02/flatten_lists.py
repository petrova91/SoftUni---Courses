some_text = input().split("|")
matrix = []
for symbols in some_text:
    elements = symbols.split()
    if elements:
        matrix.append(elements)

for i in range(len(matrix)-1, -1, -1):
    print(*matrix[i], end=" ")