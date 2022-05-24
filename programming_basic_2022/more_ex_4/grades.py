count_students = int(input())
total_evaluation = 0
top_students = 0
students_middle = 0
students_good = 0
fail_students = 0
for current_student in range(1, count_students + 1):
    evaluation = float(input())
    if 2 <= evaluation <= 2.99:
        fail_students += 1
    elif 3 <= evaluation <= 3.99:
        students_middle += 1
    elif 4 <= evaluation <= 4.99:
        students_good += 1
    elif evaluation >= 5:
        top_students += 1
    total_evaluation += evaluation
average = total_evaluation / count_students
percent_top_students = (top_students / count_students) * 100
percent_students_good = (students_good / count_students) * 100
percent_students_middle = (students_middle / count_students) * 100
percent_students_fail = (fail_students / count_students) * 100
print(f'Top students: {percent_top_students:.2f}%')
print(f'Between 4.00 and 4.99: {percent_students_good:.2f}%')
print(f'Between 3.00 and 3.99: {percent_students_middle:.2f}%')
print(f'Fail: {percent_students_fail:.2f}%')
print(f'Average: {average:.2f}')
