import re

pattern = r"(#|@)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
some_text = input()
valid_words = [word.groups() for word in re.finditer(pattern, some_text)]
mirror_words = []
for current_couple in valid_words:
    first_word = current_couple[1]
    second_word = current_couple[2]
    if first_word == second_word[::-1]:
        mirror_words.append(f"{first_word} <=> {second_word}")
if len(valid_words) == 0:
    print("No word pairs found!")
else:
    print(f"{len(valid_words)} word pairs found!")
if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
