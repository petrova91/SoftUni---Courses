def like_dish(guests_dict, data):
    name_data, guest, meal = data.split("-")
    if guest not in guests_dict:
        guests_dict[guest] = [meal]
    if meal not in guests_dict[guest]:
        guests_dict[guest].append(meal)
    return guests_dict


def dislike_dish(guests_dict, data, counter):
    name_data, guest, meal = data.split("-")
    if guest not in guests_dict:
        print(f"{guest} is not at the party.")
    elif meal not in guests_dict[guest]:
        print(f"{guest} doesn't have the {meal} in his/her collection.")
    else:
        guests_dict[guest].remove(meal)
        counter += 1
        print(f"{guest} doesn't like the {meal}.")
    return guests_dict, counter


command = input()
guests = {}
unlike_meals = 0
while not command == "Stop":
    if "Like" in command:
        guests = like_dish(guests, command)
    elif "Dislike" in command:
        guests, unlike_meals = dislike_dish(guests, command, unlike_meals)
    command = input()
for guest, meals in guests.items():
    print(f"{guest}: {', '.join(meals)}")
print(f"Unliked meals: {unlike_meals}")