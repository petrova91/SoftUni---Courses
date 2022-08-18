import re

pattern_digits = r"\d"
pattern_emoji = r"(::|\*\*)([A-Z]{1}[a-z]{2,})\1"
some_text = input()
digits = re.findall(pattern_digits, some_text)
cool_threshold = 1
for digit in digits:
    cool_threshold *= int(digit)
valid_emojis = re.findall(pattern_emoji, some_text)
print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
for emoji in valid_emojis:
    coolness = 0
    for letter in emoji[1]:
        coolness += ord(letter)
    if coolness > cool_threshold:
        print(f"{emoji[0]}{emoji[1]}{emoji[0]}")