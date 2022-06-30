words = input().split()
palindrome = input()
palindrome_words = []
counter = 0
for element in words:
    if element == element[::-1]:
        palindrome_words.append(element)
    if palindrome == element:
        counter += 1
print(palindrome_words)
print(f'Found palindrome {counter} times')