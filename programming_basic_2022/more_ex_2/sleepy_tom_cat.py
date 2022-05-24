count_free_days = int(input())
time_play_tom = 30000   #за година
play_work = 63   #за ден
play_rest = 127  #за ден
count_work_days = 365 - count_free_days
play_free_day = count_free_days * play_rest
play_work_day = count_work_days * play_work
total_play = play_free_day + play_work_day
different = abs(time_play_tom - total_play)
different_h = different // 60
different_min = different % 60
if total_play > time_play_tom:
    print('Tom will run away')
    print(f'{different_h} hours and {different_min} minutes more for play')
elif total_play <= time_play_tom:
    print('Tom sleeps well')
    print(f'{different_h} hours and {different_min} minutes less for play')


