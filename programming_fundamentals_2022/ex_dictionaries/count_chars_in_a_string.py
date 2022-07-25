text = input().split()
letters_dict = {}
for word in text:
    for letter in word:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
for letter, count in letters_dict.items():
    print(f'{letter} -> {count}')