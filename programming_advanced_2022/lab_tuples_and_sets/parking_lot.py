count_commands = int(input())
parking = set()

for _ in range(count_commands):
    direction, car_name = input().split(", ")
    if direction == "IN":
        parking.add(car_name)
    elif direction == "OUT":
        parking.discard(car_name)

if parking:
    print("\n".join(parking))
else:
    print("Parking Lot is Empty")