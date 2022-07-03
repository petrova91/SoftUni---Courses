word = input()
reversed_word = ''
for current_character in range(len(word)-1, -1, -1):
   reversed_word += word[current_character]
print(reversed_word)


#word = input()
#print(word[::-1])   # slice notation