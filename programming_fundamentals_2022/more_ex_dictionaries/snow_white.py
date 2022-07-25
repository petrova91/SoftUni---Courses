data = input()
dwarfs = {}
info_dwarfs = []
while not data == "Once upon a time":
    name, hat_color, physics = data.split(" <:> ")
    physics = int(physics)
    if hat_color not in dwarfs:
        dwarfs[hat_color] = {}
    if name not in dwarfs[hat_color]:
        dwarfs[hat_color][name] = physics
    else:
        if physics > dwarfs[hat_color][name]:
            dwarfs[hat_color][name] = physics
    data = input()
for hat, dwarf in dwarfs.items():
    for name, points in dwarf.items():
        info_dwarfs.append({"count_dwarf": len(dwarf), "name": name, "d_physics": points, "hat": hat})
for sorted_dwarf in sorted(info_dwarfs, key=lambda x: (-x["d_physics"], -x["count_dwarf"])):
    print(f'({sorted_dwarf["hat"]}) {sorted_dwarf["name"]} <-> {sorted_dwarf["d_physics"]}')
