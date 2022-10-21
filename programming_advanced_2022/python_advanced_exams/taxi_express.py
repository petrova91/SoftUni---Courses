from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]
total_time = 0

while True:
    if not customers or not taxis:
        break

    customer_time = customers.popleft()
    taxi_time = taxis.pop()

    if taxi_time >= customer_time:
        total_time += customer_time
    else:
        customers.appendleft(customer_time)

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
if not taxis and customers:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")