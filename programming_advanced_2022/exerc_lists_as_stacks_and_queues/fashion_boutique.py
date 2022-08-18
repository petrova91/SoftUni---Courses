clothes_stack = [int(value) for value in input().split()]
capacity_rack = int(input())
current_rack_capacity = capacity_rack
count_racks = 1
while clothes_stack:
    current_dress = clothes_stack[-1]
    if current_dress > current_rack_capacity:
        count_racks += 1
        current_rack_capacity = capacity_rack
    else:
        current_rack_capacity -= current_dress
        clothes_stack.pop()
print(count_racks)

