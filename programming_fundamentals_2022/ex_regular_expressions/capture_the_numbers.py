import re

text = input()
pattern = r"\d+"
numbers = []
while not text == "":
    numbers += re.findall(pattern, text)
    text = input()
print(" ".join(numbers))