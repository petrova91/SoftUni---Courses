film_name = input()
count_days = int(input())
count_tickets = int(input())
price_tickets = float(input())
percent_for_cinema = int(input())
total_win = count_days * (count_tickets * price_tickets)
win_for_cinema = (percent_for_cinema / 100) * total_win
total_win -= win_for_cinema
print(f'The profit from the movie {film_name} is {total_win:.2f} lv.')