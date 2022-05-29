key = int(input())
number_lines = int(input())
secret_message = ''
for i in range(number_lines):
    letter = input()
    secret_letter = ord(letter) + key
    secret_message += chr(secret_letter)
print(secret_message)

