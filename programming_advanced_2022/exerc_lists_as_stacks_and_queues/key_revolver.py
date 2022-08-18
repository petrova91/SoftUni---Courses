from collections import deque

price_bullet = int(input())
size_gun_barrel = int(input())
bullets_stack = [int(bullet) for bullet in input().split()]
locks = deque([int(lock) for lock in input().split()])
intelligence = int(input())
counter = 0
bullets_counter = 0
while locks:
    if not bullets_stack:
        break
    current_bullet = bullets_stack.pop()
    counter += 1
    bullets_counter += 1
    current_lock = locks[0]
    if current_bullet <= current_lock:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")
    if counter == size_gun_barrel and bullets_stack:
        print("Reloading!")
        counter = 0
bullets_cost = bullets_counter * price_bullet
earned_money = intelligence - bullets_cost
if not locks:
    print(f"{len(bullets_stack)} bullets left. Earned ${earned_money}")
elif not bullets_stack:
    print(f"Couldn't get through. Locks left: {len(locks)}")