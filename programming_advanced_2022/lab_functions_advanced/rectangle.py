def rectangle(length, width):
    if isinstance(length, str) or isinstance(width, str):
        return "Enter valid values!"

    rect_area = length * width
    rect_perim = 2 * length + 2 * width
    return f"Rectangle area: {rect_area}" + "\n" + f"Rectangle perimeter: {rect_perim}"


print(rectangle(2, 10))
print(rectangle('2', 10))
