command = input()
contest_password = {}
while command != 'end of contests':
    data = command.split(':')
    contest_name = data[0]
    password_contest = data[1]
    contest_password[contest_name] = password_contest
    command = input()
command = input()
submissions_dict = {}
while command != 'end of submissions':
    command_line = command.split('=>')
    contest_name = command_line[0]
    password = command_line[1]
    user_name = command_line[2]
    points = int(command_line[3])
    if contest_name in contest_password and password == contest_password[contest_name]:
        if user_name not in submissions_dict:
            submissions_dict[user_name] = {contest_name: points}
        else:
            if contest_name not in submissions_dict[user_name]:
                submissions_dict[user_name][contest_name] = points
            else:
                if submissions_dict[user_name][contest_name] < points:
                    submissions_dict[user_name][contest_name] = points
    command = input()
max_points = 0
best_candidate = ''
for user, contests in submissions_dict.items():
    points_user = sum(contests.values())
    if points_user > max_points:
        max_points = points_user
        best_candidate = user
print(f'Best candidate is {best_candidate} with total {max_points} points.')
print('Ranking:')
for key, value in sorted(submissions_dict.items()):
    print(key)
    for contest, points in sorted(value.items(), key=lambda kvp: -kvp[1]):
        print(f'#  {contest} -> {points}')

