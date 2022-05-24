import math

climb_record_in_seconds = float(input())
distance_in_metres = float(input())
seconds_climbing_one_metre = float(input())
delay = (distance_in_metres / 50)
delay = math.floor(delay)
delay *= 30
time_for_climbing = (distance_in_metres * seconds_climbing_one_metre) + delay
if time_for_climbing < climb_record_in_seconds:
    print(f'Yes! The new record is {time_for_climbing:.2f} seconds.')
else:
    different = time_for_climbing - climb_record_in_seconds
    print(f'No! He was {different:.2f} seconds slower.')