from collections import deque

count_pumps = int(input())
points = deque()
tour_finish = False
for _ in range(count_pumps):
    pump_data = input()
    points.append(pump_data)
for attempt in range(len(points)):
    tank = 0
    failed = False
    for index in range(len(points)):
        fuel, distance = points[index].split()
        tank = tank + int(fuel) - int(distance)
        if tank < 0:
            failed = True
    if failed:
        points.rotate(-1)
    else:
        print(attempt)
        break


