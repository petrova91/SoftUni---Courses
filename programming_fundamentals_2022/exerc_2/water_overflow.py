number_lines = int(input())
capacity_water_tank = 255
filled_water = 0
for current_line in range(number_lines):
    liters_water = int(input())
    filled_water += liters_water
    if filled_water > capacity_water_tank:
        filled_water -= liters_water
        print('Insufficient capacity!')
print(f'{filled_water}')