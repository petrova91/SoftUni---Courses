import re

some_text = input()
pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
numbers = [num.group() for num in re.finditer(pattern, some_text)]
print(" ".join(numbers))