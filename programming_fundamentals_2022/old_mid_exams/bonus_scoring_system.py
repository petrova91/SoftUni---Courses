from math import ceil

count_students = int(input())
count_lectures = int(input())
additional_bonus = int(input())
max_bonus = 0
max_attendance = 0
for student in range(1, count_students+1):
    student_attendances = int(input())
    total_bonus_student = student_attendances / count_lectures * (5 + additional_bonus)
    if total_bonus_student > max_bonus:
        max_bonus = total_bonus_student
    if student_attendances > max_attendance:
        max_attendance = student_attendances
print(f'Max Bonus: {ceil(max_bonus)}.')
print(f'The student has attended {max_attendance} lectures.')