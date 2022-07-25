some_items = input().split()
dict_food = {}
for index in range(0, len(some_items), 2):
    food = some_items[index]
    quantities = int(some_items[index+1])
    dict_food[food] = quantities
print(dict_food)