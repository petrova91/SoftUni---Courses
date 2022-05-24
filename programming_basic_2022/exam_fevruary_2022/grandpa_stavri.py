count_days = int(input())
total_liters = 0
total_degrees = 0
for current_day in range(1, count_days+1):
    count_rakiq = float(input())
    degrees_rakiq = float(input())
    total_liters += count_rakiq
    total_degrees_current_rakiq = count_rakiq * degrees_rakiq
    total_degrees += total_degrees_current_rakiq
degrees = total_degrees / total_liters
print(f'Liter: {total_liters:.2f}')
print(f'Degrees: {degrees:.2f}')
if degrees < 38:
    print('Not good, you should baking!')
elif degrees <= 42:
    print('Super!')
elif degrees > 42:
    print('Dilution with distilled water!')