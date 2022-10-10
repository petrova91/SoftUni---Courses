from collections import deque

elves = deque([int(x) for x in input().split()])
boxes = [int(x) for x in input().split()]
toys = 0
energy = 0
counter = 0

while True:
    if not elves or not boxes:
        break

    elf_energy = elves.popleft()
    if elf_energy < 5:
        continue
    box = boxes.pop()
    counter += 1

    crafted_toys = 1
    needed_energy = box
    cookie = 1

    if counter % 3 == 0:
        needed_energy *= 2
        crafted_toys = 2

    if counter % 5 == 0:
        crafted_toys = 0
        cookie = 0

    if needed_energy > elf_energy:
        boxes.append(box)
        elves.append(elf_energy*2)
        continue

    toys += crafted_toys
    elf_energy -= needed_energy
    elf_energy += cookie
    energy += needed_energy
    elves.append(elf_energy)

print(f"Toys: {toys}")
print(f"Energy: {energy}")
if elves:
    print(f"Elves left: {', '.join([str(x) for x in elves])}")
if boxes:
    print(f"Boxes left: {', '.join([str(x) for x in boxes])}")
