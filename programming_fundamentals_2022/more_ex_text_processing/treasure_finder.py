key = input().split()
key_num = list(map(int, key))
some_text = input()
while not some_text == "find":
    decrypts_message = ""
    counter = 0
    for symbol in some_text:
        decrypts_message += chr(ord(symbol) - key_num[counter])
        counter += 1
        if counter == len(key_num):
            counter = 0
    end = decrypts_message.find("&", decrypts_message.index("&")+1,len(decrypts_message))
    type = decrypts_message[decrypts_message.index("&")+1:end]
    coordinates = decrypts_message[decrypts_message.index("<")+1:decrypts_message.index(">")]
    print(f"Found {type} at {coordinates}")
    some_text = input()