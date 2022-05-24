import sys

count_movies = int(input())
total_rating = 0
max_rating = -sys.maxsize
min_rating = sys.maxsize
film_max_rating = ''
film_min_rating = ''
for current_number in range(count_movies):
    film_name = input()
    movie_rating = float(input())
    total_rating += movie_rating
    if movie_rating > max_rating:
        max_rating = movie_rating
        film_max_rating = film_name
    if movie_rating < min_rating:
        min_rating = movie_rating
        film_min_rating = film_name
average_rating = total_rating / count_movies
print(f'{film_max_rating} is with highest rating: {max_rating:.1f}')
print(f'{film_min_rating} is with lowest rating: {min_rating:.1f}')
print(f'Average rating: {average_rating:.1f}')