spell = input()
command = input()
while not command == "Abracadabra":
    data = command.split()
    name_command = data[0]
    if name_command == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif name_command == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif name_command == "Illusion":
        index = int(data[1])
        letter = data[2]
        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index+1:]
            print("Done!")
        else:
            print("The spell was too weak.")
    elif name_command == "Divination":
        first_string = data[1]
        second_string = data[2]
        if first_string in spell:
            spell = spell.replace(first_string, second_string)
            print(spell)
    elif name_command == "Alteration":
        substring = data[1]
        if substring in spell:
            spell = spell.replace(substring, "")
            print(spell)
    else:
        print("The spell did not work!")
    command = input()
