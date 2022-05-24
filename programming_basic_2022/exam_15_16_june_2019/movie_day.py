time_for_action = int(input())
count_stage = int(input())
time_of_stage = int(input())
preparation = time_for_action * 0.15
time_of_film = (count_stage * time_of_stage) + preparation
different = abs(time_for_action - time_of_film)
if time_for_action >= time_of_film:
    print(f'You managed to finish the movie on time! You have {different:.0f} minutes left!')
else:
    print(f'Time is up! To complete the movie you need {different:.0f} minutes.')