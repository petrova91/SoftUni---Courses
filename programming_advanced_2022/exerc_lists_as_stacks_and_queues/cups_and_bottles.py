from collections import deque

cups_capacity = input().split()
cups = deque([int(cup) for cup in cups_capacity])
bottles_capacity = input().split()
bottles_stack = [int(bottle) for bottle in bottles_capacity]
wasted_litters = 0
bottles_finish = False
while cups:
    if not bottles_stack:
        bottles_finish = True
        break
    current_bottle = bottles_stack.pop()
    current_cup = cups[0]
    if current_bottle >= current_cup:
        current_cup -= current_bottle
        wasted_litters += abs(current_cup)
        if current_cup <= 0:
            cups.popleft()
    else:
        cups[0] = current_cup - current_bottle
if bottles_finish:
    print(f"Cups: {' '.join(map(str, cups))}")
else:
    bottles_stack.reverse()
    print(f"Bottles: {' '.join(map(str, bottles_stack))}")
print(f"Wasted litters of water: {wasted_litters}")