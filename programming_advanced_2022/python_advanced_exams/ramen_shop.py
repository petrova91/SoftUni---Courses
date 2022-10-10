from collections import deque

bowls_of_ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])

while True:
    if not bowls_of_ramen or not customers:
        break

    bow = bowls_of_ramen.pop()
    customer = customers.popleft()

    if bow == customer:
        continue

    elif bow > customer:
        bow -= customer
        bowls_of_ramen.append(bow)

    elif bow < customer:
        customer -= bow
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in bowls_of_ramen])}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
