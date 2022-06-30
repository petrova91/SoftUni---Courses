count_rows = int(input())
war_field = []
for current_row in range(count_rows):
    row = input().split()
    row_field = [int(digit) for digit in row]
    war_field.append(row_field)
attacked_squares = input().split()
destroyed_ships = 0
for attack in attacked_squares:
    current_attack = attack.split('-')
    row = int(current_attack[0])
    col = int(current_attack[1])
    if war_field[row][col] > 0:
        war_field[row][col] -= 1
        if war_field[row][col] == 0:
            destroyed_ships += 1
print(destroyed_ships)
