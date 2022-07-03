from math import ceil

sequence_of_numbers = input().split()
finish_line = ceil(len(sequence_of_numbers) / 2)
time_left_racer = 0
time_right_racer = 0
left_side = sequence_of_numbers[:finish_line-1]
right_side = sequence_of_numbers[-1:finish_line-1:-1]
for time in left_side:
    if time != '0':
        time_left_racer += int(time)
    else:
        time_left_racer *= 0.80
for time in right_side:
    if time != '0':
        time_right_racer += int(time)
    else:
        time_right_racer *= 0.80
if time_left_racer < time_right_racer:
    print(f'The winner is left with total time: {time_left_racer:.1f}')
else:
    print(f'The winner is right with total time: {time_right_racer:.1f}')