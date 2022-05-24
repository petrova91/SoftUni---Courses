import math

count_bricks = int(input())
count_workers = int(input())
capacity_of_cart = int(input())
count_bricks_for_one_course = count_workers * capacity_of_cart
count_courses = count_bricks / count_bricks_for_one_course
print(f'{math.ceil(count_courses)}')
