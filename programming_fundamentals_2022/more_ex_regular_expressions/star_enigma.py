import re

count_messages = int(input())
pattern_decrypt = r"[star]"
pattern_code = r"(@{1}(?P<name>[A-Za-z]+)([^@\-!\:>])*:{1}(?P<population>\d+)([^@\-!\:>])*!{1}(?P<type>[AD])!{1}([^@\-!\:>])*\-{1}>{1}(?P<soldiers>\d+))"
planets = {"Attacked": [], "Destroyed": []}
for current_message in range(count_messages):
    encrypted_message = input()
    decrypted_message = ""
    key = len(re.findall(pattern_decrypt, encrypted_message, flags=re.IGNORECASE))
    for symbol in encrypted_message:
        decrypted_message += chr(ord(symbol)-key)
    valid_match = re.search(pattern_code, decrypted_message)
    if valid_match:
        attack_data = [data.groupdict() for data in re.finditer(pattern_code, decrypted_message)]
        if attack_data[0]["type"] == "A":
            planets["Attacked"].append(attack_data[0]["name"])
        elif attack_data[0]["type"] == "D":
            planets["Destroyed"].append(attack_data[0]["name"])
for attack_type, names in planets.items():
    print(f"{attack_type} planets: {len(names)}")
    names.sort()
    for name in names:
        print(f"-> {name}")


