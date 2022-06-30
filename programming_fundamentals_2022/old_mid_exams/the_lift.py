def change_state_lift(lift, count_people):
    new_state_lift = []
    for wagon in lift:
        people_in_wagon = int(wagon)
        while people_in_wagon < 4 and count_people > 0:
            people_in_wagon += 1
            count_people -= 1
        new_state_lift.append(people_in_wagon)
    print(' '.join(map(str, new_state_lift)))


total_people = int(input())
state_lift = input().split()
state_lift_as_integer = [int(element) for element in state_lift]
count_free_places = (len(state_lift_as_integer) * 4) - sum(state_lift_as_integer)
if count_free_places == total_people:
    change_state_lift(state_lift, total_people)
elif count_free_places < total_people:
    different = total_people - count_free_places
    print(f"There isn't enough space! {different} people in a queue!")
    change_state_lift(state_lift, total_people)
elif count_free_places > total_people:
    print(f'The lift has empty spots!')
    change_state_lift(state_lift, total_people)