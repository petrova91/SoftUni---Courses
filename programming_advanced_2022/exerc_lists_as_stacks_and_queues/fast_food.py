from collections import deque

quantity_food = int(input())
orders = deque([int(num) for num in input().split()])
print(max(orders))
while orders:
    current_order = orders[0]
    if current_order <= quantity_food:
        quantity_food -= current_order
        orders.popleft()
    else:
        break
if orders:
    print(f"Orders left: ", end="")
    while orders:
        order = orders.popleft()
        print(order, end=" ")
else:
    print("Orders complete")
