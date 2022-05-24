count_students = int(input())
count_top_students = 0
count_fail_students = 0
count_good_students = 0
count_average_students = 0
counter_scores = 0
for current_student in range(1, count_students + 1):
    score = float(input())
    if 2.00 <= score <= 2.99:
        count_fail_students += 1
        counter_scores += score
    elif 3.00 <= score <= 3.99:
        count_average_students += 1
        counter_scores += score
    elif 4.00 <= score <= 4.99:
        count_good_students += 1
        counter_scores += score
    elif score >= 5.00:
        count_top_students += 1
        counter_scores += score
percent_top_students = (count_top_students / count_students) * 100
percent_good_students = (count_good_students / count_students) * 100
percent_average_students = (count_average_students / count_students) * 100
percent_fail_students = (count_fail_students / count_students) * 100
average_score = counter_scores / count_students
print(f'Top students: {percent_top_students:.2f}%')
print(f'Between 4.00 and 4.99: {percent_good_students:.2f}%')
print(f'Between 3.00 and 3.99: {percent_average_students:.2f}%')
print(f'Fail: {percent_fail_students:.2f}%')
print(f'Average: {average_score:.2f}')