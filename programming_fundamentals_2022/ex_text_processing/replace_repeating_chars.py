sequence_of_letters = input()
last_chr = ""
new_letter = ""
for chr in sequence_of_letters:
    if chr == last_chr:
        continue
    else:
        new_letter += chr
        last_chr = chr
print(new_letter)