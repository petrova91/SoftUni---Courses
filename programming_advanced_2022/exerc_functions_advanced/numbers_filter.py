def even_odd_filter(**kwargs):
    sort_dict = {}
    for key, value in kwargs.items():
        if key == "odd":
            kwargs[key] = [x for x in value if x % 2 != 0]
        elif key == "even":
            kwargs[key] = [x for x in value if x % 2 == 0]
    for num_type, numbers in sorted(kwargs.items(), key=lambda x: x[1], reverse=True):
        sort_dict[num_type] = numbers
    return sort_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
