x = float(input())
y = float(input())
h = float(input())
wall_green_paint = 3.4
roof_red_paint = 4.3
side_a_door = 1.2
side_b_door = 2
area_door = side_a_door * side_b_door
area_front_wall = (x * x) - area_door
area_rear_wall = x * x
side_window = 1.5
area_window = side_window * side_window
area_side_wall = (x * y) * 2 - (area_window * 2)
total_green_paint = (area_front_wall + area_rear_wall + area_side_wall) / wall_green_paint
area_roof_rectangle = (x * y) * 2
area_roof_triangle = (x * h / 2) * 2
total_red_paint = (area_roof_rectangle + area_roof_triangle) / roof_red_paint
print(f'{total_green_paint:.2f}')
print(f'{total_red_paint:.2f}')