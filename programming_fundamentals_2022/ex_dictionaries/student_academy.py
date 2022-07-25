count_rows = int(input())
student_info = {}
for row in range(count_rows):
    student_name = input()
    grade = float(input())
    if student_name not in student_info:
        student_info[student_name] = []
    student_info[student_name].append(grade)
for name, grade in student_info.items():
    average_grade = sum(grade) / len(grade)
    if average_grade < 4.50:
        continue
    else:
        student_info[name] = average_grade
        print(f'{name} -> {average_grade:.2f}')