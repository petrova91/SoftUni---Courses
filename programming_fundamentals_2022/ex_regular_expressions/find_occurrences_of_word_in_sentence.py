import re

some_text = input()
word_to_find = input()
pattern = rf'\b{word_to_find}\b'
count_words = re.findall(pattern, some_text, re.IGNORECASE)
print(len(count_words))




