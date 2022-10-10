def palindrome(word, index):
    if index == len(word) // 2:
        return f"{word} is a palindrome"

    left_part = word[index]
    right_part = word[-1 - index]
    if left_part != right_part:
        return f"{word} is not a palindrome"

    return palindrome(word, index+1)



print(palindrome("abcba", 0))
print(palindrome("peter", 0))
