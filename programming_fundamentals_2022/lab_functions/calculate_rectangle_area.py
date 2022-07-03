def solve_area(side_a, side_b):
    area = side_a * side_b
    return area


width = int(input())
height = int(input())
print(solve_area(width, height))


# area = lambda side_a, side_b: side_a * side_b
#
# width = int(input())
# height = int(input())
# print(area(width, height))