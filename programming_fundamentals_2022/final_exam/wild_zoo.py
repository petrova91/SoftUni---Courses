def add_animal(data, animals_dict):
    animal_name, needed_food, area = data.split("-")
    if animal_name not in animals_dict:
        animals_dict[animal_name] = {"food": 0, "area": area}
    animals_dict[animal_name]["food"] += int(needed_food)
    return animals_dict


def feed_animal(data, animals_dict):
    animal_name, food = data.split("-")
    if animal_name in animals_dict:
        animals_dict[animal_name]["food"] -= int(food)
        if animals_dict[animal_name]["food"] <= 0:
            animals_dict.pop(animal_name)
            print(f"{animal_name} was successfully fed")
    return animals_dict


animals = {}
areas = {}
command = input()
while not command == "EndDay":
    name_command, others = command.split(": ")
    if name_command == "Add":
        animals = add_animal(others, animals)
    elif name_command == "Feed":
        animals = feed_animal(others, animals)
    command = input()
print(f"Animals:")
for animal in animals:
    print(f" {animal} -> {animals[animal]['food']}g")
    name_area = animals[animal]["area"]
    if name_area not in areas:
        areas[name_area] = 0
    areas[name_area] += 1
print(f"Areas with hungry animals:")
for area in areas:
    print(f" {area}: {areas[area]}")