command = input()
settlements = {}
while not command == "Sail":
    city, population, gold = command.split("||")
    if city not in settlements:
        settlements[city] = {"population": 0, "gold": 0}
    settlements[city]["population"] += int(population)
    settlements[city]["gold"] += int(gold)
    command = input()
while not command == "End":
    if command == "Sail":
        command = input()
        continue
    data = command.split("=>")
    name_command = data[0]
    town = data[1]
    gold = int(data[-1])
    if name_command == "Plunder":
        people = int(data[2])
        settlements[town]["population"] -= people
        settlements[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if settlements[town]["population"] <= 0 or settlements[town]["gold"] <= 0:
            settlements.pop(town)
            print(f"{town} has been wiped off the map!")
    elif name_command == "Prosper":
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            settlements[town]["gold"] += gold
            print(f'{gold} gold added to the city treasury. {town} now has {settlements[town]["gold"]} gold.')
    command = input()
if len(settlements) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(settlements)} wealthy settlements to go to:")
    for city, info in settlements.items():
        print(f'{city} -> Population: {info["population"]} citizens, Gold: {info["gold"]} kg')