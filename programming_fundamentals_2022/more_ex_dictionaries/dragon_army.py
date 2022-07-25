def split_data(data_line):
    dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor = data_line.split()
    if dragon_health == "null":
        dragon_health = 250
    else:
        dragon_health = int(dragon_health)
    if dragon_damage == "null":
        dragon_damage = 45
    else:
        dragon_damage = int(dragon_damage)
    if dragon_armor == "null":
        dragon_armor = 10
    else:
        dragon_armor = int(dragon_armor)
    return dragon_type, dragon_name, dragon_damage, dragon_health, dragon_armor


count_dragons = int(input())
dragons = {}
av_status = []
for dragon in range(count_dragons):
    data = input()
    d_type, name, damage, health, armor = split_data(data)
    if d_type not in dragons:
        dragons[d_type] = {}
    dragons[d_type][name] = {"damage": damage, "health": health, "armor": armor}
for type, current_dragon in dragons.items():
    av_damage = 0
    av_health = 0
    av_armor = 0
    for d_name, own_status in current_dragon.items():
        for status, points in own_status.items():
            if status == "damage":
                av_damage += points
            elif status == "health":
                av_health += points
            elif status == "armor":
                av_armor += points
    av_damage /= len(current_dragon)
    av_health /= len(current_dragon)
    av_armor /= len(current_dragon)
    av_status.append({"type": type, "av_damage": f"{av_damage:.2f}", "av_health": f"{av_health:.2f}", "av_armor": f"{av_armor:.2f}"})
for current_type in av_status:
    print(f'{current_type["type"]}::({current_type["av_damage"]}/{current_type["av_health"]}/{current_type["av_armor"]})')
    for type, d_status in dragons.items():
        if type == current_type["type"]:
            for d_name, current_status in sorted(d_status.items(), key=lambda x: x[0]):
                print(f'-{d_name} -> damage: {current_status["damage"]}, health: {current_status["health"]}, armor: {current_status["armor"]}')