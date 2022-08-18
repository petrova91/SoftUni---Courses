from collections import deque

litres_water = int(input())
line_people = deque()
name = input()
while not name == "Start":
    line_people.append(name)
    name = input()
command = input()
while not command == "End":
    if command.isdigit():
        needed_litres = int(command)
        person_name = line_people.popleft()
        if needed_litres <= litres_water:
            litres_water -= needed_litres
            print(f"{person_name} got water")
        else:
            print(f"{person_name} must wait")
    else:
        _, refill_litres = command.split()
        litres_water += int(refill_litres)
    command = input()
print(f"{litres_water} liters left")