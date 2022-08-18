capacity_messages = int(input())
command = input()
users = {}
while not command == "Statistics":
    data = command.split("=")
    name_data = data[0]
    if name_data == "Add":
        user = data[1]
        sent_message = int(data[2])
        received_message = int(data[3])
        if user not in users:
            users[user] = sent_message + received_message
    elif name_data == "Message":
        sender_user = data[1]
        receiver_user = data[2]
        if sender_user in users and receiver_user in users:
            users[sender_user] += 1
            users[receiver_user] += 1
            if users[sender_user] == capacity_messages:
                print(f"{sender_user} reached the capacity!")
                users.pop(sender_user)
            if users[receiver_user] == capacity_messages:
                print(f"{receiver_user} reached the capacity!")
                users.pop(receiver_user)
    elif name_data == "Empty":
        user = data[1]
        if user in users:
            users.pop(user)
        elif user == "All":
            users.clear()
    command = input()
print(f"Users count: {len(users)}")
for current_user, messages in users.items():
    print(f"{current_user} - {messages}")
