def check_result_dict(result_dict, user_name, user_points):
    if user_name not in result_dict:
        result_dict[user_name] = user_points
    elif user_name in result_dict:
        if user_points > result_dict[user_name]:
            result_dict[user_name] = user_points
    return result_dict


def check_submissions_dict(submission_dict, language, user_name):
    if language not in submission_dict and user_name not in submission_dict.values():
        submission_dict[language] = [user_name]
    elif language in submission_dict and user_name not in submission_dict.values():
        submission_dict[language].append(user_name)
    return submission_dict


command = input()
results = {}
submissions = {}
while command != 'exam finished':
    command_line = command.split('-')
    student_name = command_line[0]
    if 'banned' not in command_line:
        student_language = command_line[1]
        student_points = int(command_line[2])
        results = check_result_dict(results, student_name, student_points)
        submissions = check_submissions_dict(submissions, student_language, student_name)
    else:
        results.pop(student_name)
    command = input()
print('Results:')
for user, points in results.items():
    print(f'{user} | {points}')
print('Submissions:')
for languages, count_submission in submissions.items():
    print(f'{languages} - {len(count_submission)}')