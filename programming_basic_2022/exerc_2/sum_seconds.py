first_time = int(input())
second_time = int(input())
third_time = int(input())
total_time = first_time + second_time + third_time
minutes = total_time // 60
secods = total_time % 60
if secods < 10:
    print(f'{minutes}:{secods:02d}')
else:
    print(f'{minutes}:{secods}')