import re

pattern = r"(@|#)+(?P<color>[a-z]{3,})(@|#)+([^A-Za-z0-9])*/+(?P<amount>\d+)/+"
some_text = input()
founded_eggs = [egg.groupdict() for egg in re.finditer(pattern, some_text)]
for current_egg in founded_eggs:
    print(f"You found {current_egg['amount']} {current_egg['color']} eggs!")