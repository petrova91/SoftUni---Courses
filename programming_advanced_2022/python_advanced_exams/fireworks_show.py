from collections import deque


def check_collect_items(fireworks):
    for firework_name, quantity in fireworks.items():
        if fireworks[firework_name] < 3:
            return False
    return True


firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

fireworks_amount = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

while True:
    if not firework_effects or not explosive_power:
        break

    effect = firework_effects.popleft()
    if effect <= 0:
        continue
    power = explosive_power.pop()
    if power <= 0:
        firework_effects.appendleft(effect)
        continue
    result = effect + power

    if result % 3 == 0 and result % 5 != 0:
        fireworks_amount["Palm Fireworks"] += 1
    elif result % 5 == 0 and result % 3 != 0:
        fireworks_amount["Willow Fireworks"] += 1
    elif result % 3 == 0 and result % 5 == 0:
        fireworks_amount["Crossette Fireworks"] += 1
    else:
        firework_effects.append(effect - 1)
        explosive_power.append(power)

    if check_collect_items(fireworks_amount):
        print("Congrats! You made the perfect firework show!")
        break

if not check_collect_items(fireworks_amount):
    print("Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in firework_effects])}")
if explosive_power:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_power])}")
for name, count in fireworks_amount.items():
    print(f"{name}: {count}")
