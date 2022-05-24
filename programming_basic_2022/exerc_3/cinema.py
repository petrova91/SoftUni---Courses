type_movie = input()
roll = int(input())
column = int(input())
price = 0
count_places = roll * column
if type_movie == 'Premiere':
    price = 12
elif type_movie == 'Normal':
    price = 7.50
elif type_movie == 'Discount':
    price = 5
win = count_places * price
print(f'{win:.2f}')