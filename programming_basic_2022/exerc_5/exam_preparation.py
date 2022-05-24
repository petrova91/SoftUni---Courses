count_fail_grades = int(input())
name_exercise = input()
counter_bad_grades = 0
counter_exercise = 0
sum_grades = 0
name_last_exercise = ''
time_to_break = False
while name_exercise != 'Enough':
    grade = int(input())
    if grade <= 4:
        sum_grades += grade
        counter_bad_grades += 1
        if counter_bad_grades == count_fail_grades:
            time_to_break = True
            break
    else:
        sum_grades += grade
    counter_exercise += 1
    name_last_exercise = name_exercise
    name_exercise = input()
if time_to_break:
    print(f'You need a break, {counter_bad_grades} poor grades.')
else:
    average_grade = sum_grades / counter_exercise
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {counter_exercise}')
    print(f'Last problem: {name_last_exercise}')
