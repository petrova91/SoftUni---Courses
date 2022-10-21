from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees_capacities = [int(x) for x in input().split(", ")]
total_pizzas = 0

while True:
    if not pizza_orders or not employees_capacities:
        break

    order = pizza_orders.popleft()
    if order > 10 or order <= 0:
        continue
    employ = employees_capacities.pop()

    if order <= employ:
        total_pizzas += order
        continue
    if order > employ:
        order -= employ
        total_pizzas += employ
        pizza_orders.appendleft(order)

if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    if employees_capacities:
        print(f"Employees: {', '.join([str(x) for x in employees_capacities])}")
else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in pizza_orders])}")
