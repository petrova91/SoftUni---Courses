import math

needed_hours = int(input())
have_days = int(input())
count_workers = int(input())
teambuilding = have_days * 0.1
left_days = have_days - teambuilding
work_hours = (left_days * 8) + (count_workers * 2 * have_days)
work_hours = math.floor(work_hours)
difference_hour = abs(work_hours - needed_hours)
if work_hours >= needed_hours:
    print(f'Yes!{difference_hour} hours left.')
else:
    print(f'Not enough time!{difference_hour} hours needed.')

