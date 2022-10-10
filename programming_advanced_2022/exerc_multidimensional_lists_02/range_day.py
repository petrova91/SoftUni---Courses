def get_next_position(row, col, steps, direction):
    if direction == "up":
        return row - steps, col
    elif direction == "down":
        return row + steps, col
    elif direction == "left":
        return row, col - steps
    elif direction == "right":
        return row, col + steps


def is_inside(row, col, max_size):
    if 0 <= row < max_size and 0 <= col < max_size:
        return True
    return False


size = 5
field = []
hero_row = None
hero_col = None
total_targets = 0
shot_targets = []

for row_i in range(size):
    row_element = input().split()
    field.append(row_element)
    if "A" in row_element:
        hero_row = row_i
        hero_col = row_element.index("A")
    if "x" in row_element:
        total_targets += row_element.count("x")

field[hero_row][hero_col] = "."
count_commands = int(input())
for _ in range(count_commands):
    command = input().split()
    name_command = command[0]
    position = command[1]
    if name_command == "move":
        steps = int(command[2])
        next_row, next_col = get_next_position(hero_row, hero_col, steps, position)
        if is_inside(next_row, next_col, size) and field[next_row][next_col] == ".":
            hero_row = next_row
            hero_col = next_col
    elif name_command == "shoot":
        bullet_row, bullet_col = get_next_position(hero_row, hero_col, 1, position)
        while is_inside(bullet_row, bullet_col, size):
            if field[bullet_row][bullet_col] == "x":
                total_targets -= 1
                field[bullet_row][bullet_col] = "."
                shot_targets.append([bullet_row, bullet_col])
                break
            bullet_row, bullet_col = get_next_position(bullet_row, bullet_col, 1, position)
        if total_targets == 0:
            break

if total_targets == 0:
    print(f"Training completed! All {len(shot_targets)} targets hit.")
else:
    print(f"Training not completed! {total_targets} targets left.")
print(*shot_targets, sep="\n")