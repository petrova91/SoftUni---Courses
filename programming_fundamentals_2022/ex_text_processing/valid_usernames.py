usernames = input().split(", ")
for user in usernames:
    if 3 <= len(user) < 17 and user.isidentifier() or "-" in user:
        print(user)
