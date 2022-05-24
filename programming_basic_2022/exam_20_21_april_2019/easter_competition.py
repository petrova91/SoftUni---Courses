count_participant = int(input())
max_point = 0
best_chef = ''
for current_participant in range(1, count_participant + 1):
    name_chef = input()
    command = input()
    total_count_current_points = 0
    while command != 'Stop':
        score = int(command)
        total_count_current_points += score
        command = input()
    print(f'{name_chef} has {total_count_current_points} points.')
    if total_count_current_points > max_point:
        print(f'{name_chef} is the new number 1!')
        best_chef = name_chef
        max_point = total_count_current_points
print(f'{best_chef} won competition with {max_point} points!')

