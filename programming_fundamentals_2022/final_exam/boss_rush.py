import re

pattern = r"\|([A-Z]{4,})\|:#([A-Za-z]+\s{1}[A-Za-z]+)#"
count_inputs = int(input())
for _ in range(count_inputs):
    some_text = input()
    valid_text = re.findall(pattern, some_text)
    if valid_text:
        print(f"{valid_text[0][0]}, The {valid_text[0][1]}")
        print(f">> Strength: {len(valid_text[0][0])}")
        print(f">> Armor: {len(valid_text[0][1])}")
    else:
        print("Access denied!")

