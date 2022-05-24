minutes_control = int(input())
seconds_control = int(input())
length = float(input())
seconds_for_100_metres = int(input())
control_in_seconds = (minutes_control * 60) + seconds_control
time_reduction = (length / 120) * 2.5
total_time = ((length / 100) * seconds_for_100_metres) - time_reduction
if total_time <= control_in_seconds:
    print('Marin Bangiev won an Olympic quota!')
    print(f'His time is {total_time:.3f}.')
else:
    different = total_time - control_in_seconds
    print(f'No, Marin failed! He was {different:.3f} second slower.')