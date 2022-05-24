film_name = input()
max_points = 0
best_film = ''
count_films = 0
while film_name != 'STOP':
    count_films += 1
    sum_symbols = 0
    if count_films == 7:
        print(f'The limit is reached.')
        break
    length_film_name = len(film_name)
    for index in range(length_film_name):
        if 65 <= ord(film_name[index]) <= 90:
            value = ord(film_name[index]) - length_film_name
            sum_symbols += value
        elif 97 <= ord(film_name[index]) <= 122:
            value = ord(film_name[index]) - length_film_name * 2
            sum_symbols += value
        elif ord(film_name[index]) == 32:
            sum_symbols += 32
        elif 48 <= ord(film_name[index]) <= 57:
            value = ord(film_name[index])
            sum_symbols += value
    if sum_symbols > max_points:
        max_points = sum_symbols
        best_film = film_name
    film_name = input()
print(f'The best movie for you is {best_film} with {max_points} ASCII sum.')