size = int(input())
field = []
alice_row = None
alice_col = None
tea_quantity = 0
alice_success = False

for row_index in range(size):
    row = input().split()
    field.append(row)
    if "A" in row:
        alice_row = row_index
        alice_col = row.index("A")

field[alice_row][alice_col] = "*"
command = input()
while True:
    if command == "up":
        alice_row -= 1
    elif command == "down":
        alice_row += 1
    elif command == "left":
        alice_col -= 1
    elif command == "right":
        alice_col += 1

    if alice_row >= size or alice_row < 0 or alice_col >= size or alice_col < 0:
        break
    elif field[alice_row][alice_col] == "R":
        field[alice_row][alice_col] = "*"
        break
    elif field[alice_row][alice_col].isdigit():
        tea_quantity += int(field[alice_row][alice_col])
        field[alice_row][alice_col] = "*"
        if tea_quantity >= 10:
            alice_success = True
            break
    else:
        field[alice_row][alice_col] = "*"

    command = input()

if alice_success:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
for i in range(size):
    print(*field[i])
