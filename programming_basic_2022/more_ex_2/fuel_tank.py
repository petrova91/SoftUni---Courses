fuel = input()
litres = float(input())
if fuel == 'Diesel':
    if litres >= 25:
        print(f'You have enough {fuel.lower()}.')
    elif litres < 25:
        print(f'Fill your tank with {fuel.lower()}!')
elif fuel == 'Gasoline':
    if litres >= 25:
        print(f'You have enough {fuel.lower()}.')
    elif litres < 25:
        print(f'Fill your tank with {fuel.lower()}!')
elif fuel == 'Gas':
    if litres >= 25:
        print(f'You have enough {fuel.lower()}.')
    elif litres < 25:
        print(f'Fill your tank with {fuel.lower()}!')
else:
    print('Invalid fuel!')