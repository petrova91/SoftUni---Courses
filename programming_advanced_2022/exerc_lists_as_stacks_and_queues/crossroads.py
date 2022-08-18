from collections import deque

time_green_light = int(input())
time_free_window = int(input())
light = time_green_light
window = time_free_window
command = input()
cars = deque()
total_cars_passed = 0
while not command == "END":
    if not command == "green":
        cars.append(command)
        light = time_green_light
        window = time_free_window
    elif command == "green" and cars:
        car = cars.popleft()
        total_cars_passed += 1
        current_car = car
        if len(car) < light:
            light -= len(car)
            if light > 0:
                continue
        else:
            car = car[light:]
            if len(car) > window:
                car = car[window:]
                print("A crash happened!")
                print(f"{current_car} was hit at {car[0]}.")
                break
    command = input()
else:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")