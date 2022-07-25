import re

phone_numbers = input()
pattern = r"\+359(?P<separator> |-)2(?P=separator)\d{3}(?P=separator)\d{4}\b"
valid_numbers = [num.group() for num in re.finditer(pattern, phone_numbers)]
print(", ".join(valid_numbers))