text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
new_text = [letter for letter in text if letter.lower() not in vowels]
print(''.join(new_text))