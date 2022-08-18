def add_user(users, data):
    user_name = data.split(": ")[1]
    if user_name not in users:
        users[user_name] = {"likes": 0, "comments": 0}
    return users


def add_likes(users, data):
    name_data, user_name, count_likes = data.split(": ")
    add_user(users, data)
    users[user_name]["likes"] += int(count_likes)
    return users


def add_comment(users, data):
    user_name = data.split(": ")[1]
    add_user(users, data)
    users[user_name]["comments"] += 1
    return users


def delete_user(users, data):
    user_name = data.split(": ")[1]
    if user_name not in users:
        print(f"{user_name} doesn't exist.")
    else:
        users.pop(user_name)
    return users


command = input()
followers = {}
while not command == "Log out":
    name_command = command.split(": ")[0]
    if name_command == "New follower":
        followers = add_user(followers, command)
    elif name_command == "Like":
        followers = add_likes(followers, command)
    elif name_command == "Comment":
        followers = add_comment(followers, command)
    elif name_command == "Blocked":
        followers = delete_user(followers, command)
    command = input()
print(f"{len(followers)} followers")
for user, info in followers.items():
    print(f'{user}: {info["likes"] + info["comments"]}')
