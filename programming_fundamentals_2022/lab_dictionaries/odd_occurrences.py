words = input().split()
words_dict = {}
for word in words:
    lower_word = word.lower()
    if lower_word not in words_dict:
        words_dict[lower_word] = 1
    else:
        words_dict[lower_word] += 1
for key, value in words_dict.items():
    if value % 2 != 0:
        print(key, end=' ')
