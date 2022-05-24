country = input()
appliance = input()   # уред
max_points = 20
points_of_difficulty = 0
points_of_performance = 0
if country == 'Russia':
    if appliance == 'ribbon':
        points_of_difficulty = 9.100
        points_of_performance = 9.400
    elif appliance == 'hoop':
        points_of_difficulty = 9.300
        points_of_performance = 9.800
    elif appliance == 'rope':
        points_of_difficulty = 9.600
        points_of_performance = 9.000
elif country == 'Bulgaria':
    if appliance == 'ribbon':
        points_of_difficulty = 9.600
        points_of_performance = 9.400
    elif appliance == 'hoop':
        points_of_difficulty = 9.550
        points_of_performance = 9.750
    elif appliance == 'rope':
        points_of_difficulty = 9.500
        points_of_performance = 9.400
elif country == 'Italy':
    if appliance == 'ribbon':
        points_of_difficulty = 9.200
        points_of_performance = 9.500
    elif appliance == 'hoop':
        points_of_difficulty = 9.450
        points_of_performance = 9.350
    elif appliance == 'rope':
        points_of_difficulty = 9.700
        points_of_performance = 9.150
total_points = points_of_difficulty + points_of_performance
percent_different = ((max_points - total_points) / max_points) * 100
print(f'The team of {country} get {total_points:.3f} on {appliance}.')
print(f'{percent_different:.2f}%')