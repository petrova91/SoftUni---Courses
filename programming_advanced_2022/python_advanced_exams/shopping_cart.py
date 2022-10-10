def shopping_cart(*args):
    result = ""
    limit_of_products = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    products = {"Soup": [], "Pizza": [], "Dessert": []}
    for el in args:
        if el == "Stop":
            if len(products["Soup"]) == 0 and len(products["Pizza"]) == 0 and len(products["Dessert"]) == 0:
                return "No products in the cart!"

            for meal, meal_products in sorted(products.items(), key=lambda x: (-len(x[1]), x[0])):
                result += f"{meal}:" + "\n"
                for product in sorted(meal_products):
                    result += f" - {product}" + "\n"
            return result

        type_meal, products_for_meal = el
        if products_for_meal not in products[type_meal] and limit_of_products[type_meal] > 0:
            products[type_meal].append(products_for_meal)
            limit_of_products[type_meal] -= 1


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print()

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print()

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

