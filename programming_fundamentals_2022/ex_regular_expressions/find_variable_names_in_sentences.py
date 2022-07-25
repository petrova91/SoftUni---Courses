import re

some_text = input()
pattern = r"(?<=\b_)[a-zA-Z0-9]+\b"
variable_names = [obj.group() for obj in re.finditer(pattern, some_text)]
print(",".join(variable_names))