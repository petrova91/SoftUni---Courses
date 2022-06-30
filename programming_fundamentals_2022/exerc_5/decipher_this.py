def fix_message(text):
    decipher_message = []
    for word in text:
        character_code = ''
        changed_word = []
        for letter in word:
            if '0' <= letter <= '9':
                character_code += letter
            else:
                changed_word.append(letter)
        first_letter = chr(int(character_code))
        changed_word.insert(0, first_letter)
        changed_word[1], changed_word[-1] = changed_word[-1], changed_word[1]
        new_word = ''.join(changed_word)
        decipher_message.append(new_word)
    return decipher_message


secret_message = input().split()
print(' '.join(fix_message(secret_message)))