lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expense = 0
counter_shield_brake = 0
for current_lost_fight in range(1, lost_fights+1):
    if current_lost_fight % 2 == 0:
        expense += helmet_price
    if current_lost_fight % 3 == 0:
        expense += sword_price
    if current_lost_fight % 2 == 0 and current_lost_fight % 3 == 0:
        expense += shield_price
        counter_shield_brake += 1
        if counter_shield_brake == 2:
            expense += armor_price
            counter_shield_brake = 0
print(f'Gladiator expenses: {expense:.2f} aureus')
