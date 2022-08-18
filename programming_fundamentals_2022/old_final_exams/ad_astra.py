import re

pattern = r"(?P<sep>#|\|)(?P<name>[A-Za-z\s]+)(?P=sep)(?P<date>(\d{2}/\d{2}/\d{2}))(?P=sep)(?P<cal>\d+)(?P=sep)"
some_text = input()
items = [food.groupdict() for food in re.finditer(pattern, some_text)]
total_calories = sum([int(item["cal"]) for item in items])
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")
for food in items:
    print(f'Item: {food["name"]}, Best before: {food["date"]}, Nutrition: {food["cal"]}')

