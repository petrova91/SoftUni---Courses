import re

pattern = r"^(\$|%)(?P<tag>[A-Z]{1}[a-z]{2,})\1:\s{1}(\[(?P<first_num>\d+)\]\|)(\[(?P<second_num>\d+)\]\|)(\[(?P<third_num>\d+)\]\|)$"
count_messages = int(input())
for _ in range(count_messages):
    message = input()
    valid_message = re.match(pattern, message)
    if not valid_message:
        print("Valid message not found!")
    else:
        symbols = [sym.groupdict() for sym in re.finditer(pattern, message)]
        decrypted_message = chr(int(symbols[0]["first_num"])) + chr(int(symbols[0]["second_num"])) + chr(int(symbols[0]["third_num"]))
        print(f'{symbols[0]["tag"]}: {decrypted_message}')
