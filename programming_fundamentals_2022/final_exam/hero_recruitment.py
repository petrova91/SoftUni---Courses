def check_hero(hero, hero_dict):
    if hero not in hero_dict:
        return True
    return False


def save_hero(heroes_book, data):
    hero_name = data.split()[1]
    if check_hero(hero_name, heroes_book):
        heroes_book[hero_name] = []
    else:
        print(f"{hero_name} is already enrolled.")
    return heroes_book


def learn_spell(heroes_book, data):
    name_data, hero_name, spell_name = data.split()
    if check_hero(hero_name, heroes_book):
        print(f"{hero_name} doesn't exist.")
    else:
        if spell_name in heroes_book[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes_book[hero_name].append(spell_name)
    return heroes_book


def unlearn_spell(heroes_book, data):
    name_data, hero_name, spell_name = data.split()
    if check_hero(hero_name, heroes_book):
        print(f"{hero_name} doesn't exist.")
    else:
        if spell_name not in heroes_book[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes_book[hero_name].remove(spell_name)
    return heroes_book


command = input()
spellbook = {}
while not command == "End":
    name_command = command.split()[0]
    if name_command == "Enroll":
        spellbook = save_hero(spellbook, command)
    elif name_command == "Learn":
        spellbook = learn_spell(spellbook, command)
    elif name_command == "Unlearn":
        spellbook = unlearn_spell(spellbook, command)
    command = input()
print("Heroes:")
for hero, spell in spellbook.items():
    print(f"== {hero}: {''.join(spell)}")