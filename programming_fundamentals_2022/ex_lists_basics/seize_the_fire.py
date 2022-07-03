fire_in_different_cells = input().split('#')
water = int(input())
effort = 0
total_fire = 0
suppress_cells = []
for cell in fire_in_different_cells:
    current_fire_cell = cell.split(' = ')
    level_fire = current_fire_cell[0]
    value_of_fire = int(current_fire_cell[1])
    if level_fire == 'High':
        if 81 <= value_of_fire <= 125:
            if water >= value_of_fire:
                water -= value_of_fire
                effort += value_of_fire * 0.25
                total_fire += value_of_fire
                suppress_cells.append(value_of_fire)
            else:
                continue
    elif level_fire == 'Medium':
        if 51 <= value_of_fire <= 80:
            if water >= value_of_fire:
                water -= value_of_fire
                effort += value_of_fire * 0.25
                total_fire += value_of_fire
                suppress_cells.append(value_of_fire)
            else:
                continue
    elif level_fire == 'Low':
        if 1 <= value_of_fire <= 50:
            if water >= value_of_fire:
                water -= value_of_fire
                effort += value_of_fire * 0.25
                total_fire += value_of_fire
                suppress_cells.append(value_of_fire)
        else:
            continue
    if water <= 0:
        break
print('Cells:')
for i in range(len(suppress_cells)):
    print(f' - {suppress_cells[i]}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')