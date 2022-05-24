import math

total_training_days = int(input())
start_kilometres = float(input())
goal = 1000
total_kilometres = start_kilometres
kilometres_for_day = start_kilometres
for current_day in range(1, total_training_days + 1):
    percent_more = int(input())
    kilometres_for_day = kilometres_for_day + ((percent_more /100) * kilometres_for_day)
    total_kilometres += kilometres_for_day
different = abs(goal - total_kilometres)
if total_kilometres >= goal:
    print(f"You've done a great job running {math.ceil(different)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {math.ceil(different)} more kilometers")
