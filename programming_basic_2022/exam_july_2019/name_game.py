gamer_name = input()
winner = ''
max_points = 0
while gamer_name != 'Stop':
    count_points = 0
    count_numbers = len(gamer_name)
    for index in range(count_numbers):
        number = int(input())
        if gamer_name[index] == chr(number):
            count_points += 10
        else:
            count_points += 2
    if count_points >= max_points:
        max_points = count_points
        winner = gamer_name
    gamer_name = input()
print(f'The winner is {winner} with {max_points} points!')