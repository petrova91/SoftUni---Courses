import re

pattern = r"(!)([A-Z]{1}[a-z]{2,})\1:\[([a-zA-Z]{8,})\]"
count_text = int(input())
for _ in range(count_text):
    text = input()
    valid_message = re.match(pattern, text)
    if valid_message:
        some_string = valid_message.group(3)
        print(f"{valid_message.group(2)}:", end=" ")
        for index, letter in enumerate(some_string):
            if index == len(some_string)-1:
                print(f"{ord(letter)}")
            else:
                print(f"{ord(letter)}", end=" ")
    else:
        print("The message is invalid")