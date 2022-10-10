def naughty_or_nice_list(santa_list, *args, **kwargs):
    result = ""
    kids = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }

    for el in args:
        searched_item = ""
        item_index = 0
        count_appearance = 0
        num, kid_type = el.split("-")
        for index, name in enumerate(santa_list):
            digit, kid_name = name
            if int(num) == digit:
                searched_item = kid_name
                item_index = index
                count_appearance += 1
        if count_appearance == 1:
            kids[kid_type].append(searched_item)
            santa_list.pop(item_index)

    if kwargs:
        for kid, type_kid in kwargs.items():
            searched_item = ""
            item_index = 0
            count_appearance = 0
            for index, name in enumerate(santa_list):
                digit, kid_name = name
                if kid == kid_name:
                    searched_item = kid
                    count_appearance += 1
                    item_index = index
            if count_appearance == 1:
                kids[type_kid].append(searched_item)
                santa_list.pop(item_index)

    for number, left_kid in santa_list:
        kids["Not found"].append(left_kid)

    for key, value in kids.items():
        if value:
            result += f"{key}: {', '.join(value)}" + "\n"
    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
