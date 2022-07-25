information = input()
course_information = {}
while information != 'end':
    data = information.split(' : ')
    course_name = data[0]
    student_name = data[1]
    if course_name not in course_information:
        course_information[course_name] = []
    course_information[course_name].append(student_name)
    information = input()
for course_name, student_name in course_information.items():
    print(f'{course_name}: {len(student_name)}')
    for student in student_name:
        print(f'-- {student}')