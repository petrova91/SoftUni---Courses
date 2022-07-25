import re

pattern = r"((w{3})\.[A-Za-z0-9]+(\-[A-Za-z0-9]+)*(\.[a-z]+)+)"
valid_emails = []
sentence = input()
while True:
    if sentence == "":
        break
    else:
        valid_emails += [e_mail.group() for e_mail in re.finditer(pattern, sentence)]
        sentence = input()
print("\n".join(valid_emails))