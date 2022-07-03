import math

def find_distance_between_two_points(num_a, num_b):
    center_x = 0
    center_y = 0
    arg_a = math.pow(num_a - center_x, 2)
    arg_b = math.pow(num_b - center_y, 2)
    return math.sqrt(arg_a + arg_b)


first_point_x = float(input())
first_point_y = float(input())
second_point_x = float(input())
second_point_y = float(input())
distance_first_point = find_distance_between_two_points(first_point_x, first_point_y)
distance_second_point = find_distance_between_two_points(second_point_x, second_point_y)
if distance_first_point < distance_second_point:
    print(f'({math.floor(first_point_x)}, {math.floor(first_point_y)})')
else:
    print(f'({math.floor(second_point_x)}, {math.floor(second_point_y)})')