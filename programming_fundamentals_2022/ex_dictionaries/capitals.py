country_names = input().split(', ')
capital_cities = input().split(', ')
tuple_country_capital = zip(country_names, capital_cities)
country_dict = {key: value for (key, value) in tuple_country_capital}
for country, capital in country_dict.items():
    print(f'{country} -> {capital}')