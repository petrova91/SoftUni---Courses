count_rows = int(input())
matrix = []

for _ in range(count_rows):
    row = list(input())
    matrix.append(row)

searched_symbol = input()
symbol_is_found = False

for index_row in range(count_rows):
    for index_col in range(count_rows):
        if searched_symbol == matrix[index_row][index_col]:
            symbol_is_found = True
            print(f"({index_row}, {index_col})")
    if symbol_is_found:
        break

if not symbol_is_found:
    print(f"{searched_symbol} does not occur in the matrix")
