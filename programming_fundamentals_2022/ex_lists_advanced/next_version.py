current_version = input()
current_version = current_version.replace('.', '')
next_version = int(current_version) + 1
next_version = str(next_version)
print('.'.join(next_version))
