energy = int(input())
command = input()
wins = 0
energy_is_not_finish = True
while command != 'End of battle':
    distance = int(command)
    if distance <= energy:
        energy -= distance
        wins += 1
        if wins % 3 == 0:
            energy += wins
    else:
        energy_is_not_finish = False
        print(f'Not enough energy! Game ends with {wins} won battles and {energy} energy')
        break
    command = input()
if energy_is_not_finish:
    print(f'Won battles: {wins}. Energy left: {energy}')

