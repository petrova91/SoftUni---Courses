def start_spring(**kwargs):
    objects = {}
    result = ""
    for key, value in kwargs.items():
        if value not in objects:
            objects[value] = []
        objects[value].append(key)
    sort_objects = sorted(objects.items(), key=lambda x: (-len(x[1]), x[0]))
    for spring_obj, spring_el in sort_objects:
        result += f"{spring_obj}:" + "\n"
        for el in sorted(spring_el):
            result += f"-{el}" + "\n"
    return result


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))


