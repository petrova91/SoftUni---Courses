import re

pattern = r"(?P<sep>[=/])([A-Z]{1}[A-Za-z]{2,})(?P=sep)"
some_text = input()
valid_destinations = [place.group(2) for place in re.finditer(pattern, some_text)]
travel_points = sum([len(elem) for elem in valid_destinations])
print(f'Destinations: {", ".join(valid_destinations)}')
print(f'Travel Points: {travel_points}')
