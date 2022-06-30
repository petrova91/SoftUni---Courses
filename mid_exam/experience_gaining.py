needed_experience = float(input())
count_battles = int(input())
tank_is_unlock = False
total_experience = 0
battles = 0
for current_battle in range(1, count_battles+1):
    earned_experience = float(input())
    total_experience += earned_experience
    battles = current_battle
    if current_battle % 3 == 0:
        total_experience += earned_experience * 0.15
    if current_battle % 5 == 0:
        total_experience -= earned_experience * 0.10
    if current_battle % 15 == 0:
        total_experience += earned_experience * 0.05
    if total_experience >= needed_experience:
        tank_is_unlock = True
        break
if tank_is_unlock:
    print(f'Player successfully collected his needed experience for {battles} battles.')
else:
    different = needed_experience - total_experience
    print(f'Player was not able to collect the needed experience, {different:.2f} more needed.')

