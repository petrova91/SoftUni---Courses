count_lines = int(input())
for line in range(count_lines):
    some_text = input()
    name = some_text[some_text.index("@")+1:some_text.index("|")]
    age = some_text[some_text.index("#")+1:some_text.index("*")]
    print(f'{name} is {age} years old.')
