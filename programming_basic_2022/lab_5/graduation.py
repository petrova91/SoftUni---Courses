name_student = input()
year_grade = 0
year = 1
fail_counter = 0
while year <= 12:
    if fail_counter > 1:
        break
    current_grade = float(input())
    if current_grade < 4:
        fail_counter += 1
        continue
    year_grade += current_grade
    year += 1
average_grade = year_grade / 12
if fail_counter < 2:
    print(f'{name_student} graduated. Average grade: {average_grade:.2f}')
else:
    print(f'{name_student} has been excluded at {year} grade')