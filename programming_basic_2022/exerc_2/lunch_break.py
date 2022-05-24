import math

name_serial = input()
time_epizod = int(input())
time_relax = int(input())
time_lunch = time_relax / 8
time_relaxation = time_relax / 4
time_free = time_relax - time_lunch - time_relaxation
remaining_time = abs(time_epizod - time_free)
up = math.ceil(remaining_time)
if time_free >= time_epizod:
    print("You have enough time to watch"+" "+name_serial+" "+"and left with"+" "+str(up)+" "+"minutes free time.")
else:
    print("You don't have enough time to watch"+" "+name_serial+","+" "+"you need"+" "+str(up)+" "+"more minutes.")
