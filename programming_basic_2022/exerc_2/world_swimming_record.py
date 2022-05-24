old_record = float(input())
distance = float(input())
time_per_meter = float(input())
bonus_time = (distance // 15) * 12.5
needed_time = (distance * time_per_meter) + bonus_time
if needed_time < old_record:
    print(f'Yes, he succeeded! The new world record is {needed_time:.2f} seconds.')
elif needed_time >= old_record:
    different = abs(old_record - needed_time)
    print(f'No, he failed! He was {different:.2f} seconds slower.')
