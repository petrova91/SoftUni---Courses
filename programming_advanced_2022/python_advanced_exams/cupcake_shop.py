def stock_availability(flavours, command, *args):
    if command == "delivery":
        for elem in args:
            flavours.append(elem)
    elif command == "sell":
        if args:
            for elem in args:
                if isinstance(elem, int):
                    flavours = flavours[elem:]
                else:
                    if elem in flavours:
                        flavours_copy = flavours.copy()
                        for product in flavours_copy:
                            if elem == product:
                                flavours.remove(elem)
        else:
            flavours = flavours[1:]
    return flavours


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
