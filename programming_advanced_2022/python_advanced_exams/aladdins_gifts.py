from collections import deque


def get_present(magic_level):
    if 100 <= magic_level <= 199:
        return "Gemstone"
    elif 200 <= magic_level <= 299:
        return "Porcelain Sculpture"
    elif 300 <= magic_level <= 399:
        return "Gold"
    elif 400 <= magic_level <= 499:
        return "Diamond Jewellery"


materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

gifts = {}

while True:
    if not materials or not magic:
        break

    material = materials.pop()
    spell = magic.popleft()
    result = material + spell
    gift = get_present(result)

    if gift is None:
        if result < 100:
            if result % 2 == 0:
                material *= 2
                spell *= 3
                result = material + spell
            else:
                result *= 2
        elif result > 499:
            result /= 2
        gift = get_present(result)

    if gift is not None:
        if gift not in gifts:
            gifts[gift] = 0
        gifts[gift] += 1

if ("Gemstone" in gifts and "Porcelain Sculpture" in gifts) \
        or ("Gold" in gifts and "Diamond Jewellery" in gifts):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")
if gifts:
    for key, value in sorted(gifts.items(), key=lambda x: x[0]):
        print(f"{key}: {value}")