def made_set(num_range):
    start, end = num_range.split(",")
    start = int(start)
    end = int(end)
    nums = {num for num in range(start, end + 1)}
    return nums


count_inputs = int(input())
max_intersection = set()

for _ in range(count_inputs):
    first_range, second_range = input().split("-")

    first_set = made_set(first_range)
    second_set = made_set(second_range)

    intersection = first_set.intersection(second_set)
    if len(intersection) > len(max_intersection):
        max_intersection = intersection

print(f"Longest intersection is [{', '.join(map(str,max_intersection))}] with length {len(max_intersection)}")

