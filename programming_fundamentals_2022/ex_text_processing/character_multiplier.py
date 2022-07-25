some_text = input()
first_word, second_word = some_text.split()
sum_letters = 0
if len(first_word) > len(second_word):
    for i in range(len(second_word)):
        sum_letters += ord(first_word[i]) * ord(second_word[i])
    for chr in first_word[len(second_word):]:
        sum_letters += ord(chr)
elif len(second_word) > len(first_word):
    for i in range(len(first_word)):
        sum_letters += ord(first_word[i]) * ord(second_word[i])
    for chr in second_word[len(first_word):]:
        sum_letters += ord(chr)
else:
    for i in range(len(first_word)):
        sum_letters += ord(first_word[i]) * ord(second_word[i])
print(sum_letters)