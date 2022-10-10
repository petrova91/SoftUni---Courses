from collections import deque

chocolates_stack = [int(num) for num in input().split(", ")]
cups_milk = deque([int(num) for num in input().split(", ")])

succeed = True
counter = 0
while not counter == 5:
    if not chocolates_stack or not cups_milk:
        succeed = False
        break
    chocolate = chocolates_stack.pop()
    cup = cups_milk.popleft()
    if chocolate <= 0 or cup <= 0:
        if cup > 0:
            cups_milk.appendleft(cup)
        elif chocolate > 0:
            chocolates_stack.append(chocolate)
    elif not chocolate == cup:
        cups_milk.append(cup)
        chocolates_stack.append(chocolate - 5)
    else:
        counter += 1

if succeed:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates_stack:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates_stack)}")
else:
    print("Chocolate: empty")
if cups_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_milk)}")
else:
    print("Milk: empty")