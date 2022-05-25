group_size = int(input())
adventure_days = int(input())
earn_coins = 0
for current_day in range(1, adventure_days+1):
    earn_coins += 50
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    spend_for_food = 2 * group_size
    earn_coins -= spend_for_food
    if current_day % 3 == 0:
        spend_for_water = 3 * group_size
        earn_coins -= spend_for_water
    if current_day % 5 == 0:
        slay_monster = 20 * group_size
        earn_coins += slay_monster
        if current_day % 3 == 0:
            motivational_party = 2 * group_size
            earn_coins -= motivational_party
personal_coins = int(earn_coins / group_size)
print(f'{group_size} companions received {personal_coins} coins each.')
