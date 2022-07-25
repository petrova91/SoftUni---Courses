some_text = input()
digits = ""
letters = ""
other_char = ""
for chr in some_text:
    if chr.isdigit():
        digits += chr
    elif chr.isalpha():
        letters += chr
    else:
        other_char += chr
print(digits)
print(letters)
print(other_char)