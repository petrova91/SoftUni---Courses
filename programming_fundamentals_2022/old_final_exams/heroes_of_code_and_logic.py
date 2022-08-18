count_heroes = int(input())
heroes = {}
for _ in range(count_heroes):
    hero, hp, mp = input().split()
    heroes[hero] = {"hp": int(hp), "mp": int(mp)}
command = input()
while not command == "End":
    data = command.split(" - ")
    name_command = data[0]
    hero_name = data[1]
    if name_command == "CastSpell":
        needed_mp = int(data[2])
        spell_name = data[3]
        if heroes[hero_name]["mp"] >= needed_mp:
            heroes[hero_name]["mp"] -= needed_mp
            print(f'{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]["mp"]} MP!')
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif name_command == "TakeDamage":
        damage = int(data[2])
        attacker = data[3]
        heroes[hero_name]["hp"] -= damage
        if heroes[hero_name]["hp"] > 0:
            print(f'{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]["hp"]} HP left!')
        else:
            heroes.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")
    elif name_command == "Recharge":
        amount = int(data[2])
        old_amount_mp = heroes[hero_name]["mp"]
        heroes[hero_name]["mp"] += amount
        if heroes[hero_name]["mp"] > 200:
            heroes[hero_name]["mp"] = 200
        dif_amount = heroes[hero_name]["mp"] - old_amount_mp
        print(f"{hero_name} recharged for {dif_amount} MP!")
    elif name_command == "Heal":
        amount = int(data[2])
        old_amount_hp = heroes[hero_name]["hp"]
        heroes[hero_name]["hp"] += amount
        if heroes[hero_name]["hp"] > 100:
            heroes[hero_name]["hp"] = 100
        dif_amount = heroes[hero_name]["hp"] - old_amount_hp
        print(f"{hero_name} healed for {dif_amount} HP!")
    command = input()
for current_hero, info in heroes.items():
    print(f"{current_hero}")
    print(f'HP: {info["hp"]}')
    print(f"MP: {info['mp']}")
