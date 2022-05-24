name_actor = input()
points_of_academy = float(input())
count_judges = int(input())
total_points = points_of_academy
final_points = 1250.5
nomination_is_win = False
for current_judge in range(count_judges):
    name_judge = input()
    points_of_judge = float(input())
    length_name = len(name_judge)
    points_current_judge = (length_name * points_of_judge) / 2
    total_points += points_current_judge
    if total_points > final_points:
        nomination_is_win = True
        break
if nomination_is_win:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!')
else:
    different = final_points - total_points
    print(f'Sorry, {name_actor} you need {different:.1f} more!')