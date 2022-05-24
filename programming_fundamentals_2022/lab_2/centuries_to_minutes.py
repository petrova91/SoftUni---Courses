centuries = int(input())
one_year_days = 365.2422
years = centuries * 100
days = int(years * one_year_days)
hours = days * 24
minutes = hours * 60
print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
