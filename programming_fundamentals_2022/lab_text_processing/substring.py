string_to_remove = input()
some_string = input()
while string_to_remove in some_string:
    some_string = some_string.replace(string_to_remove, "")
print(some_string)