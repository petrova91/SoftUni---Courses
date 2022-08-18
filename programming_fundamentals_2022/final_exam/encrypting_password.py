import re

pattern = r"(?P<sym>.+)\>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<\>]{3})\<(?P=sym)"
count_passwords = int(input())
for _ in range(count_passwords):
    password = input()
    valid_password = re.match(pattern, password)
    if valid_password:
        parts_of_password = valid_password.group(2) + valid_password.group(3) + valid_password.group(4) + valid_password.group(5)
        print(f"Password: {parts_of_password}")
    else:
        print("Try another password!")