travel_tour = input()
command = input()
while not command == "Travel":
    data = command.split(":")
    name_data = data[0]
    if name_data == "Add Stop":
        index = int(data[1])
        string = data[2]
        if 0 <= index < len(travel_tour):
            travel_tour = travel_tour[:index] + string + travel_tour[index:]
    elif name_data == "Remove Stop":
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index < len(travel_tour) and 0 <= end_index < len(travel_tour):
            travel_tour = travel_tour[:start_index] + travel_tour[end_index+1:]
    elif name_data == "Switch":
        old_string = data[1]
        new_string = data[2]
        travel_tour = travel_tour.replace(old_string, new_string)
    print(travel_tour)
    command = input()
print(f"Ready for world tour! Planned stops: {travel_tour}")