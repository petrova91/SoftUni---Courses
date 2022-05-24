name_actor = input()
total_points = float(input())
count_judge = int(input())
max_points = 1250.5
for judge in range(count_judge):
    name_judge = input()
    points_judge = float(input())
    length_name = len(name_judge)
    total_points_judge = (length_name * points_judge) / 2
    total_points += total_points_judge
    if total_points > max_points:
        break
if total_points > max_points:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!')
else:
    needed_points = abs(max_points - total_points)
    print(f'Sorry, {name_actor} you need {needed_points:.1f} more!')