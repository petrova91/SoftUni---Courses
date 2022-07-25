information = input()
course_information = {}
while ':' in information:
    info_line = information.split(':')
    name = info_line[0]
    id = int(info_line[1])
    course = info_line[2]
    if course not in course_information:
        course_information[course] = {}
    course_information[course][id] = name
    information = input()
information = ' '.join(information.split('_'))
for key, value in course_information.items():
    if key == information:
        for id, name in value.items():
            print(f'{name} - {id}')

# information = input()
# course_information = {}
# students_counter = 0
# while ':' in information:
#     info_line = information.split(':')
#     name = info_line[0]
#     ID = int(info_line[1])
#     course = info_line[2]
#     students_counter += 1
#     course_information[students_counter] = {}
#     course_information[students_counter]['name'] = name
#     course_information[students_counter]['ID'] = ID
#     course_information[students_counter]['course'] = course
#     information = input()
# information = ' '.join(information.split('_'))
# for student in course_information:
#     if course_information[student]['course'] == information:
#         print(f"{course_information[student]['name']} - {course_information[student]['ID']}")