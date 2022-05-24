hour_of_examine = int(input())
minute_of_examine = int(input())
hour_of_arriving = int(input())
minute_of_arriving = int(input())
time_of_examine = hour_of_examine * 60 + minute_of_examine
time_of_arriving = hour_of_arriving * 60 + minute_of_arriving
if time_of_arriving > time_of_examine:
    print('Late')
elif time_of_examine - 30 <= time_of_arriving <= time_of_examine:
    print('On time')
else:
    print('Early')
different = abs(time_of_arriving - time_of_examine)
hours = different // 60
minutes = different % 60
if time_of_examine - 60 < time_of_arriving < time_of_examine:
    print(f'{minutes} minutes before the start')
elif time_of_arriving <= time_of_examine:
    print(f'{hours}:{minutes:02d} hours before the start')
elif time_of_examine < time_of_arriving < time_of_examine + 60:
    print(f'{minutes} minutes after the start')
elif time_of_arriving >= time_of_examine + 60:
    print(f'{hours}:{minutes:02d} hours after the start')