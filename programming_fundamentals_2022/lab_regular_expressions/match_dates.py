import re

some_dates = input()
pattern = r"(?P<day>\d{2})(?P<separator>\.|\-|\/)(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
valid_dates = [date.groupdict() for date in re.finditer(pattern, some_dates)]
for current_date in valid_dates:
    print(f'Day: {current_date["day"]}, Month: {current_date["month"]}, Year: {current_date["year"]}')