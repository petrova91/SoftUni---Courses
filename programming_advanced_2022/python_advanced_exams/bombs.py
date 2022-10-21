from collections import deque


def check_collect_bombs(collected_bombs):
    for name, count in collected_bombs.items():
        if collected_bombs[name] < 3:
            return False
    return True


bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

bombs = {
    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"
}

created_bombs = {
    "Datura Bombs": 0,
    "Cherry Bombs": 0,
    "Smoke Decoy Bombs": 0
}
while True:
    if not bomb_casings or not bomb_effects:
        break

    effect = bomb_effects.popleft()
    casing = bomb_casings.pop()
    result = effect + casing

    if result in bombs:
        name_bomb = bombs[result]
        created_bombs[name_bomb] += 1
    else:
        casing -= 5
        bomb_casings.append(casing)
        bomb_effects.appendleft(effect)

    if check_collect_bombs(created_bombs):
        print("Bene! You have successfully filled the bomb pouch!")
        break

if not check_collect_bombs(created_bombs):
    print("You don't have enough materials to fill the bomb pouch.")
if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
for key, value in sorted(created_bombs.items(), key=lambda x: x[0]):
    print(f"{key}: {value}")