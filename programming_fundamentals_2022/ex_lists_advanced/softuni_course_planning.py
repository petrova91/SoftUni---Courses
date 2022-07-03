def swap_command(schedule, current_command):
    title = current_command[1]
    second_lesson_title = command_line[2]
    if title in schedule and second_lesson_title in schedule:
        # lessons
        first_index = schedule.index(title)
        second_index = schedule.index(second_lesson_title)
        schedule[first_index], schedule[second_index] = schedule[second_index], schedule[first_index]
        # exercise
        if f'{title}-Exercise' in schedule:
            title_exercise = f'{title}-Exercise'
            schedule.remove(title_exercise)
            index_lesson = schedule.index(title)
            schedule.insert(index_lesson + 1, title_exercise)

        if f'{second_lesson_title}-Exercise' in schedule:
            title_exercise = f'{second_lesson_title}-Exercise'
            schedule.remove(title_exercise)
            index_lesson = schedule.index(second_lesson_title)
            schedule.insert(index_lesson + 1, title_exercise)
    return schedule


course_schedule = input().split(', ')
command = input()
while 'course start' not in command:
    command_line = command.split(':')
    command_name = command_line[0]
    lesson_title = command_line[1]
    if command_name == 'Add':
        if lesson_title not in course_schedule:
            course_schedule.append(lesson_title)
    elif command_name == 'Insert':
        index = int(command_line[2])
        if lesson_title not in course_schedule:
            course_schedule.insert(index, lesson_title)
    elif command_name == 'Remove':
        if lesson_title in course_schedule:
            course_schedule.remove(lesson_title)
    elif command_name == 'Swap':
        swap_command(course_schedule, command_line)
    elif command_name == 'Exercise':
        if lesson_title in course_schedule and f'{lesson_title}-Exercise' not in course_schedule:
            index_lesson = course_schedule.index(lesson_title)
            course_schedule.insert(index_lesson + 1, f'{lesson_title}-Exercise')
        elif lesson_title not in course_schedule:
            course_schedule.append(lesson_title)
            course_schedule.append(f'{lesson_title}-Exercise')
    command = input()
for index, element in enumerate(course_schedule):
    print(f'{index + 1}.{element}')
