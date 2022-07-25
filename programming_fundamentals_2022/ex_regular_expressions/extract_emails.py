import re

pattern = r"(^|(?<=\s))(?P<user>[a-z0-9]+[\.\-_a-z0-9]+)@(?P<host>([a-z\-])+(\.[a-z]+)+)"
sentence = input()
e_mails = [e_mail.group() for e_mail in re.finditer(pattern, sentence)]
print("\n".join(e_mails))