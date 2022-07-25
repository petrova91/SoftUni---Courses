command = input()
tournament = {}
individual_statistic = {}
while command != 'no more time':
    data = command.split(' -> ')
    user_name = data[0]
    contest = data[1]
    points = int(data[2])
    if contest not in tournament:
        tournament[contest] = {}
    if user_name not in tournament[contest]:
        tournament[contest][user_name] = points
    else:
        if points > tournament[contest][user_name]:
            tournament[contest][user_name] = points

    if user_name not in individual_statistic:
        individual_statistic[user_name] = 0
    command = input()
for key, value in tournament.items():
    print(f'{key}: {len(value)} participants')
    first_counter = 1
    for name, points in sorted(value.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        individual_statistic[name] += points
        print(f'{first_counter}. {name} <::> {points}')
        first_counter += 1
print('Individual standings:')
second_counter = 1
for student, score in sorted(individual_statistic.items(), key=lambda kvp: (-kvp[1], kvp[0])):
    print(f'{second_counter}. {student} -> {score}')
    second_counter += 1