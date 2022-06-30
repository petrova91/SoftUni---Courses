def spread_love(current_command, houses, last_index):
    command_line = current_command.split()
    length = int(command_line[1])
    house_index = last_index + length
    if house_index >= len(houses):
        house_index = 0
    if houses[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    else:
        houses[house_index] -= 2
        if houses[house_index] == 0:
            print(f"Place {house_index} has Valentine's day.")
    last_index = house_index
    return houses, last_index


neighborhood = input().split('@')
neighbors = [int(num) for num in neighborhood]
command = input()
last_position_index = 0
while command != 'Love!':
    neighbors, last_position_index = spread_love(command, neighbors, last_position_index)
    command = input()
print(f"Cupid's last position was {last_position_index}.")
if sum(neighbors) == 0:
    print("Mission was successful.")
else:
    count_love_house = neighbors.count(0)
    count_sad_house = len(neighbors) - count_love_house
    print(f"Cupid has failed {count_sad_house} places.")
