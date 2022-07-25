some_text = input()
text_list = []
dict_resources = {}
while some_text != 'stop':
    text_list.append(some_text)
    some_text = input()
for index in range(0, len(text_list), 2):
    resource = text_list[index]
    quantities = int(text_list[index+1])
    if resource not in dict_resources:
        dict_resources[resource] = quantities
    else:
        dict_resources[resource] += quantities
for resource, quantity in dict_resources.items():
    print(f'{resource} -> {quantity}')

