import math

serial_name = input()
count_season = int(input())
count_episodes = int(input())
time_of_episode = float(input())
advertisement = time_of_episode * 0.20  #реклама
bonus_time = count_season * 10
total_time = ((time_of_episode + advertisement) * count_episodes) * count_season + bonus_time
total_time = math.floor(total_time)
print(f'Total time needed to watch the {serial_name} series is {total_time} minutes.')