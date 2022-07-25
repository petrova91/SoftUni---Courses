import re

pattern_health = r"[^0-9\+\-\*\/\.]"
pattern_digits = r"(?P<digit>[\-]?\d+(\.\d+)*)"
pattern_signs = r"[\/\*]"
demons = input().split(",")
demons_book = {}
for demon in demons:
    demon_name = demon.strip()
    health = 0
    damage = 0
    decrypted_health = re.findall(pattern_health, demon_name)
    for symbol in decrypted_health:
        health += ord(symbol)
    decrypted_nums = [num.group() for num in re.finditer(pattern_digits, demon_name)]
    for num in decrypted_nums:
        damage += float(num)
    symbols = re.findall(pattern_signs, demon_name)
    for sign in symbols:
        if sign == "*":
            damage *= 2
        elif sign == "/":
            damage /= 2
    demons_book[demon_name] = {"health": health, "damage": damage}
for name_demon, power in sorted(demons_book.items(), key=lambda x: x[0]):
    print(f'{name_demon} - {demons_book[name_demon]["health"]} health, {demons_book[name_demon]["damage"]:.2f} damage')