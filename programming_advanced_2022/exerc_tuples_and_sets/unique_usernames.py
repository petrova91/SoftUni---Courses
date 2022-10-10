count_usernames = int(input())

usernames = set()

for _ in range(count_usernames):
    user_name = input()
    usernames.add(user_name)

print("\n".join(usernames))