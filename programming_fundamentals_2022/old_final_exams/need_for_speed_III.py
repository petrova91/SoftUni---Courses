count_cars = int(input())
cars = {}
for _ in range(count_cars):
    car, mileage, fuel = input().split("|")
    cars[car] = {"mileage": int(mileage), "fuel": int(fuel)}
command = input()
while not command == "Stop":
    data = command.split(" : ")
    command_name = data[0]
    car_name = data[1]
    if command_name == "Drive":
        distance = int(data[2])
        fuel = int(data[3])
        if fuel > cars[car_name]["fuel"]:
            print("Not enough fuel to make that ride")
        else:
            cars[car_name]["mileage"] += distance
            cars[car_name]["fuel"] -= fuel
            print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car_name]["mileage"] >= 100000:
            cars.pop(car_name)
            print(f"Time to sell the {car_name}!")
    elif command_name == "Refuel":
        fuel = int(data[2])
        old_amount_fuel = cars[car_name]["fuel"]
        cars[car_name]["fuel"] += fuel
        if cars[car_name]["fuel"] > 75:
            cars[car_name]["fuel"] = 75
        amount_fuel = cars[car_name]["fuel"] - old_amount_fuel
        print(f"{car_name} refueled with {amount_fuel} liters")
    elif command_name == "Revert":
        kilometres = int(data[2])
        cars[car_name]["mileage"] -= kilometres
        if cars[car_name]["mileage"] < 10000:
            cars[car_name]["mileage"] = 10000
        else:
            print(f"{car_name} mileage decreased by {kilometres} kilometers")
    command = input()
for current_car in cars:
    a = 1
    print(f'{current_car} -> Mileage: {cars[current_car]["mileage"]} kms, Fuel in the tank: {cars[current_car]["fuel"]} lt.')