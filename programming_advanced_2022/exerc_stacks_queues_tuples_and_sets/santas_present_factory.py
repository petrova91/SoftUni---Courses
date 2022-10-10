from collections import deque

materials_stack = [int(num) for num in input().split()]
magic_levels = deque(int(num) for num in input().split())

presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}
crafted_presents = {}

while materials_stack:
    if not magic_levels:
        break
    box = materials_stack.pop()
    magic = magic_levels.popleft()
    if box == 0 and magic == 0:
        continue
    if magic == 0:
        materials_stack.append(box)
        continue
    if box == 0:
        magic_levels.appendleft(magic)
        continue

    result = box * magic
    if result in presents:
        toy = presents[result]
        if toy not in crafted_presents:
            crafted_presents[toy] = 0
        crafted_presents[toy] += 1
        continue

    if result < 0:
        result = box + magic
        materials_stack.append(result)
    else:
        materials_stack.append(box + 15)

if ("Doll" in crafted_presents and "Wooden train" in crafted_presents)\
     or ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_stack:
    materials_stack.reverse()
    print(f"Materials left: {', '.join(str(x) for x in materials_stack)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
for toy, count in sorted(crafted_presents.items()):
    print(f"{toy}: {count}")


