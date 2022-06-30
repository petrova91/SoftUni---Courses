first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
count_students = int(input())
total_count_students_per_hour = first_employee + second_employee + third_employee
work_hours = 0
while count_students > 0:
    work_hours += 1
    if work_hours % 4 == 0:
        continue
    else:
        count_students -= total_count_students_per_hour
print(f'Time needed: {work_hours}h.')
