legendary_materials = {'shards': 0, 'fragments': 0, 'motes': 0}
junk_dict = {}
legendary_items = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}
legendary_item_is_win = False
while not legendary_item_is_win:
    sequence_of_items = input().split()
    for index in range(0, len(sequence_of_items), 2):
        quantity = int(sequence_of_items[index])
        material = sequence_of_items[index + 1].lower()
        if material in legendary_materials:
            legendary_materials[material] += quantity
            if legendary_materials[material] >= 250 and not legendary_item_is_win:
                legendary_item_is_win = True
                print(f'{legendary_items[material]} obtained!')
                legendary_materials[material] -= 250
                break
        else:
            if material not in junk_dict:
                junk_dict[material] = quantity
            else:
                junk_dict[material] += quantity
for key, value in legendary_materials.items():
    print(f'{key}: {value}')
for key, value in junk_dict.items():
    print(f'{key}: {value}')
