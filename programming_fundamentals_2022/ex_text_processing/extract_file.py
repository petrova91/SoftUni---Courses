file_name = input().replace(chr(92), ".")
file_name = file_name.split(".")
print(f'File name: {file_name[-2]}')
print(f'File extension: {file_name[-1]}')