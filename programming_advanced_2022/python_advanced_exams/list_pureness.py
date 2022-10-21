from collections import deque
from sys import maxsize


def best_list_pureness(numbers, count_rotations):
    numbers = deque(numbers)
    best_sum = -maxsize
    rotation = 0
    for current_rotation in range(count_rotations+1):
        sum_nums = 0
        for idx, num in enumerate(numbers):
            sum_nums += idx * num
        if sum_nums > best_sum:
            best_sum = sum_nums
            rotation = current_rotation
        numbers.rotate(1)
    return f"Best pureness {best_sum} after {rotation} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)




