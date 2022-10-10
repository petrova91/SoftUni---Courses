from collections import deque

rows, columns = [int(x) for x in input().split()]
text = deque(input())

for row_index in range(rows):
    row = []
    while len(row) < columns:
        row.append(text[0])
        text.rotate(-1)
    if row_index % 2 != 0:
        row.reverse()
    print("".join(row))


