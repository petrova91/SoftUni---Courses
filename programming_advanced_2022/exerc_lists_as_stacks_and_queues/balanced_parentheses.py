parentheses = [symbol for symbol in input()]
parentheses_stack = []
balanced = True
pairs = {
    "(": ")",
    "[": "]",
    "{": "}"
}
for elem in parentheses:
    if elem in "([{":
        parentheses_stack.append(elem)
    elif not parentheses_stack:
        balanced = False
    else:
        if pairs[parentheses_stack.pop()] != elem:
            balanced = False
    if not balanced:
        break
if balanced:
    print("YES")
else:
    print("NO")