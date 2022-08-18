count_plants = int(input())
plants_rarity = {}
plants_rating = {}
for _ in range(count_plants):
    plant, rarity = input().split("<->")
    plants_rarity[plant] = int(rarity)
    plants_rating[plant] = []
command = input()
while not command == "Exhibition":
    data = command.split()
    name_command = data[0]
    plant_name = data[1]
    if plant_name not in plants_rarity:
        print("error")
    elif name_command == "Rate:":
        rating = int(data[-1])
        plants_rating[plant_name].append(rating)
    elif name_command == "Update:":
        new_rarity = int(data[-1])
        plants_rarity[plant_name] = new_rarity
    elif name_command == "Reset:":
        plants_rating[plant_name].clear()
    command = input()
print("Plants for the exhibition:")
for name in plants_rarity:
    if len(plants_rating[name]) == 0:
        average_rating = 0
    else:
        average_rating = sum(plants_rating[name]) / len(plants_rating[name])
    print(f"- {name}; Rarity: {plants_rarity[name]:.0f}; Rating: {average_rating:.2f}")

