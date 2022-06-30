from math import floor, sqrt


def find_distance_between_two_points(num_x1, num_x2, num_y1, num_y2):
    arg_a = (num_x2 - num_x1)**2
    arg_b = (num_y2 - num_y1)**2
    return sqrt(arg_a + arg_b)


def print_closer_point(num_x1, num_x2, num_y1, num_y2):
    first_point_distance_to_center = find_distance_between_two_points(0, num_x1, 0, num_y1)
    second_point_distance_to_center = find_distance_between_two_points(0, num_x2, 0, num_y2)
    if first_point_distance_to_center <= second_point_distance_to_center:
        print(f'({floor(num_x1)}, {floor(num_y1)})({floor(num_x2)}, {floor(num_y2)})')
    else:
        print(f'({floor(num_x2)}, {floor(num_y2)})({floor(num_x1)}, {floor(num_y1)})')


# first_line = fl
fl_x1 = float(input())
fl_y1 = float(input())
fl_x2 = float(input())
fl_y2 = float(input())
# second_line = sl
sl_x1 = float(input())
sl_y1 = float(input())
sl_x2 = float(input())
sl_y2 = float(input())
length_first_line = find_distance_between_two_points(fl_x1, fl_x2, fl_y1, fl_y2)
length_second_line = find_distance_between_two_points(sl_x1, sl_x2, sl_y1, sl_y2)
if length_first_line >= length_second_line:
    print_closer_point(fl_x1, fl_x2, fl_y1, fl_y2)
else:
    print_closer_point(sl_x1, sl_x2, sl_y1, sl_y2)